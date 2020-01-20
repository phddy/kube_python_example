from .base_cache import LocalCache
from uuid import uuid4


class TestCache(LocalCache):
    def __init__(self):
        super().__init__(default_timeout=600, prefix='test_cache')

    def create_item(self, *key):
        return str(uuid4())


test_cache = TestCache()
