// DXF Sketch offline cache. VERSION must match APP_VERSION in index.html; bump both on every release.
const VERSION = '1.8.0';
const CACHE = 'dxf-sketch-' + VERSION;
const CORE = ['./', './index.html', './manifest.webmanifest'];
const EXTRA = ['./icons/icon-180.png', './icons/icon-192.png', './icons/icon-512.png', './icons/icon-maskable-512.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(CORE).then(() =>
    Promise.all(EXTRA.map(u => c.add(u).catch(() => {}))))));   // a missing icon must not stop offline use
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys()
    .then(keys => Promise.all(keys.filter(k => k.startsWith('dxf-sketch-') && k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});
self.addEventListener('message', e => { if (e.data === 'skip') self.skipWaiting(); });

// Cache first: the app opens instantly and with no signal. Updates arrive through the
// new service worker (Settings › Check for updates / Reload to update).
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== location.origin) return;
  e.respondWith(
    caches.open(CACHE).then(c => c.match(req, {ignoreSearch: true}).then(hit => {
      if (hit) return hit;
      if (req.mode === 'navigate') return c.match('./index.html').then(r => r || fetch(req));
      return fetch(req).then(res => { if (res.ok) c.put(req, res.clone()); return res; });
    }))
  );
});
