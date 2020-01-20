from falcon.routing.compiled import CompiledRouter


class CIRouter(CompiledRouter):
    def find(self, uri, req=None):
        uri = uri.lower()
        return super().find(uri, req)


def add_routes(app):
    from . import cache_controller as cache
    import os

    app.add_route('/cache', cache.CacheController())

    version_path = os.path.join(os.getcwd(), 'version')
    version = 'hello world'
    if os.path.exists(version_path):
        with open(version_path, 'r') as file:
            tmp = file.read()
            if tmp:
                version = tmp[:7]

    class Heartbeat:
        def on_get(self, request, response):
            response.body = version

    app.add_route('/heartbeat', Heartbeat())
    app.add_route('/', Heartbeat())
