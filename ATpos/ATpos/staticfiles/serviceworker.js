var CACHE_NAME = 'cache-v4';
self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {
      return cache.addAll([
        '/base_layout',
        '/static/idb.js',
        '/static/idbop.js'
      ]);
    })
  );
});
self.addEventListener('activate', event => {
  console.log('V1 now ready to handle fetches!');
});
self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    

    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '/productos/')) {
        event.respondWith(caches.match('/base_layout'));
        return;
      }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});
