// DXF Sketch offline cache. VERSION must match APP_VERSION in index.html; bump both on every release.
const VERSION = '3.0.3';
const CACHE = 'dxf-sketch-' + VERSION;
const CORE = ['./', './index.html', './manifest.webmanifest'];
const EXTRA = ['./icons/icon-180.png', './icons/icon-192.png', './icons/icon-512.png', './icons/icon-maskable-512.png'];

// Always take fresh copies from GitHub when a new version installs: skip the browser cache
// (cache: 'reload') and GitHub's CDN (?v= makes it a new address), then store them under the plain name.
const fresh = u => fetch(new Request(u + (u.includes('?') ? '&' : '?') + 'v=' + VERSION, {cache: 'reload'}))
  .then(r => { if (!r.ok) throw new Error(u + ' ' + r.status); return r; });

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c =>
    Promise.all(CORE.map(u => fresh(u).then(r => c.put(u, r)))).then(() =>
      Promise.all(EXTRA.map(u => fresh(u).then(r => c.put(u, r)).catch(() => {}))))));   // a missing icon must not stop offline use
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys()
    .then(keys => Promise.all(keys.filter(k => k.startsWith('dxf-sketch-') && k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});
self.addEventListener('message', e => { if (e.data === 'skip') self.skipWaiting(); });

// Cache first: the app opens instantly and with no signal. Updates arrive through the
// new service worker (the orange Update button, or Settings › Check for updates).
self.addEventListener('fetch', e => {
  const req = e.request;
  const url = new URL(req.url);
  if (req.method !== 'GET' || url.origin !== location.origin) return;
  if (url.pathname.endsWith('/VERSION')) return;   // always ask the network: this is how the app spots a new release
  e.respondWith(
    caches.open(CACHE).then(c => c.match(req, {ignoreSearch: true}).then(hit => {
      if (hit) return hit;
      if (req.mode === 'navigate') return c.match('./index.html').then(r => r || fetch(req));
      return fetch(req).then(res => { if (res.ok) c.put(req, res.clone()); return res; });
    }))
  );
});
