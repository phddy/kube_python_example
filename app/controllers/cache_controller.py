from .base_controller import BaseController
import ujson as json
from cache.test_cache import test_cache


class CacheController(BaseController):
    def __init__(self):
        super().__init__()
        self.ssp_id = 'admixer_cpm'

    def on_get(self, request, response):
        key = request.get_param('key')
        value = test_cache.get(key)

        body = json.dumps({
            'data': {
                'key': key,
                'value': value
            },
            'status': 200
        })
        response.body = body
        response.content_type = 'application/json'
