#!/usr/bin/env python3
"""Automatic checks run before every release: the app opens without errors, every step and 3D draw,
and the DXF it writes is valid, on the right layers and colours, and starts at 0,0."""
import functools, http.server, io, re, sys, threading
from pathlib import Path

import ezdxf
from ezdxf import recover
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
fails = []
def check(ok, msg):
    print(('ok   ' if ok else 'FAIL ') + msg)
    if not ok:
        fails.append(msg)

# versions agree everywhere
v = (ROOT / 'VERSION').read_text().strip()
page = (ROOT / 'index.html').read_text(encoding='utf-8')
check(re.search(r"const APP_VERSION='([^']+)'", page).group(1) == v, 'APP_VERSION matches VERSION ' + v)
check(re.search(r"const VERSION = '([^']+)'", (ROOT / 'sw.js').read_text()).group(1) == v, 'sw.js VERSION matches')
check(re.search(r'VERSION = "([^"]+)"', (ROOT / 'laptop/DXF-Sketch.py').read_text()).group(1) == v, 'laptop helper VERSION matches')
check((ROOT / 'laptop/DXF-Sketch.html').read_text(encoding='utf-8') == page, 'laptop/DXF-Sketch.html is the same page')
check(re.search(r'"v": "' + re.escape(v) + '"', page) is not None, "What's new has an entry for " + v)
check(('## ' + v + ' ') in (ROOT / 'CHANGELOG.md').read_text(encoding='utf-8'), 'CHANGELOG.md has a section for ' + v)

handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT))
class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass
handler = functools.partial(Quiet, directory=str(ROOT))
srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
threading.Thread(target=srv.serve_forever, daemon=True).start()
url = 'http://127.0.0.1:%d/index.html?test' % srv.server_address[1]

SAMPLE = '''()=>{const T=window.__dxfTest,{S,render,uid,FURN}=T;const r=S.p.rooms[0];S.p.name='Test Hospital';r.name='Microbiology';r.num='12';
  const W=(l,t)=>({id:uid(),len:l,turn:t,t:null,m:null});r.walls=[W(6000,0),W(4000,90),W(6000,90),W(4000,90)];const w=r.walls.map(x=>x.id);
  r.openings=[{id:uid(),type:'door',wall:w[2],off:1500,w:1000,leaves:1,swing:'in'},{id:uid(),type:'window',wall:w[1],off:800,w:1500}];
  r.items=[{id:uid(),kind:'pillar',shape:'rect',wall:w[1],along:2800,w:400,d:400,off:0}];
  r.points=['s1p','s1u','rj','water','drain','air'].map((k,i)=>({id:uid(),kind:k,wall:w[0],along:600+i*800,off:0}));
  const F=(k,wall,al,o,x)=>Object.assign({id:uid(),kind:k,wall:wall,along:al,off:o||0,rot:FURN[k].rot||0},x||{});
  r.furn=[F('bench',w[0],200,0,{w:4000,d:700}),F('pc',w[0],500,0),F('sink',w[0],2600,0),F('bcab',w[0],700,0),F('osmo',w[2],4200,0),F('equip',w[3],500,0,{w:600,d:650,name:'Fridge'})];
  r.place={mode:'free',x:12345,y:-6789,rot:17};S.p.labs[0].north=60;S.room=r.id;render();return 1;}'''

with sync_playwright() as p:
    b = p.chromium.launch(**({'executable_path': '/usr/bin/google-chrome', 'args': ['--no-sandbox']} if __import__('os').environ.get('LOCAL_CHROME') else {}))
    for vp in [(1180, 820), (820, 1180), (390, 844)]:
        pg = b.new_page(viewport={'width': vp[0], 'height': vp[1]})
        errs = []
        pg.on('pageerror', lambda e, errs=errs: errs.append(str(e)))
        pg.goto(url)
        pg.wait_for_timeout(800)
        pg.evaluate(SAMPLE)
        for step in range(1, 9):
            pg.evaluate('(s)=>window.__dxfTest.A.step(s)', step)
            pg.wait_for_timeout(120)
        pg.evaluate('()=>{window.__dxfTest.A.v3d();}'); pg.wait_for_timeout(300)
        for m in ['low', 'cut', 'full']:
            pg.evaluate('(m)=>window.__dxfTest.A.w3d(m)', m); pg.wait_for_timeout(120)
        pg.evaluate('()=>{window.__dxfTest.A.v3d();}'); pg.wait_for_timeout(200)
        for sh in ['settings', 'about', 'sharesheet', 'projects']:
            pg.evaluate('(a)=>{window.__dxfTest.A[a]();}', sh); pg.wait_for_timeout(150)
            pg.evaluate('(a)=>{window.__dxfTest.A[a]();}', sh); pg.wait_for_timeout(80)
        check(not errs, 'no script errors at %dx%d %s' % (vp[0], vp[1], errs[:2] if errs else ''))
        if vp[0] == 1180:
            dxf = pg.evaluate('()=>window.__dxfTest.toDXF(window.__dxfTest.S.p)')
            plan = pg.evaluate('()=>window.__dxfTest.planPrintHTML()')
        pg.close()
    b.close()
srv.shutdown()

doc, aud = recover.read(io.BytesIO(dxf.encode('utf-8')))
check(not aud.has_errors, 'DXF reads without errors ' + '; '.join(str(e.message) for e in aud.errors[:3]))
msp = doc.modelspace()
layers = {e.dxf.layer for e in msp}
check({'Room', 'Area', 'Room Dimensions'} <= layers, 'DXF layers ' + ', '.join(sorted(layers)))
furn = [e for e in msp.query('INSERT') if e.dxf.name in ('PC', 'Sink', 'Bench Cabinet', 'Osmosis') or e.dxf.name.startswith('Bench ')]
check(len(furn) >= 5 and all(e.dxf.color == 125 and e.dxf.layer == 'Room' for e in furn), 'furniture and equipment on Room in colour 125')
svc = [e for e in msp.query('INSERT') if e.dxf.name in ('Socket 1P', 'Socket 1P UPS', 'Socket RJ45', 'Water Tubing', 'Waste Tubing', 'Air Tubing')]
check(len(svc) == 6 and all(e.dxf.layer == 'Room' for e in svc), 'six services on layer Room')
xs, ys = [], []
for e in msp.query('LWPOLYLINE'):
    for q in e.get_points('xy'):
        xs.append(q[0]); ys.append(q[1])
check(abs(min(xs)) < 0.01 and abs(min(ys)) < 0.01, 'plan starts at 0,0 (min %.2f, %.2f)' % (min(xs), min(ys)))
check('1:' in plan and '<svg' in plan, 'plan to scale is made')

print('\n%d problem(s)' % len(fails) if fails else '\nall checks passed')
sys.exit(1 if fails else 0)
