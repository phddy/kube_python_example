from werkzeug.contrib.cache import RedisCache
from application import config


class LocalCache(RedisCache):
    def __init__(self, default_timeout, prefix):
        cache_host = config.get('BASE_LOCAL_CACHE_HOST')
        cache_socket = config.get('BASE_LOCAL_CACHE_SOCKET')

        if cache_socket:
            super().__init__(default_timeout=default_timeout, unix_socket_path=cache_socket,
                             db=config['BASE_LOCAL_CACHE_DB'])
        else:
            super().__init__(default_timeout=default_timeout, host=cache_host, port=config["BASE_LOCAL_CACHE_PORT"],
                             db=config['BASE_LOCAL_CACHE_DB'])

        self.prefix = prefix + ":"

    def get(self, *key, **kwargs):
        prefixed_key = self.prefix + ':'.join([str(k) if k is not None else '' for k in key])
        item = super().get(prefixed_key)

        if item is None:
            item = self.create_item(*key)
            super().set(prefixed_key, 'NULL' if item is None else item)
        elif item == 'NULL':
            return None
        return item

    def create_item(self, *key):
        '''
        multi key일때는 (self, *key) key[0], key[1]로 사용
        single key일때는 (self, key) key로 사용
        '''
        raise NotImplementedError("Should have implemented this")

    def set(self, key, item=None, timeout=None):
        raise DeprecationWarning
