import os, types, errno


class Config(dict):

    def __init__(self, defaults=None):
        dict.__init__(self, defaults or {})

    def from_pyfile(self, filename, silent=False):
        d = types.ModuleType('config')
        d.__file__ = filename
        try:
            with open(filename, mode='rb') as config_file:
                exec(compile(config_file.read(), filename, 'exec'), d.__dict__)
        except IOError as e:
            if silent and e.errno in (
                    errno.ENOENT, errno.EISDIR, errno.ENOTDIR
            ):
                return False
            e.strerror = 'Unable to load configuration file (%s)' % e.strerror
            raise
        for key in dir(d):
            if key.isupper():
                self[key] = getattr(d, key)
        return True


env = os.environ.get('ENV') or 'local'
settings = 'config/' + env + '.py'
config = Config()
config.from_pyfile(settings)