import falcon
from controllers import CIRouter, add_routes
import cProfile
import io
import pstats
import logging
from config import config

# class ProfilerMiddleware(object):
#     def __init__(self):
#         self.profile = False
#         self.profiler = cProfile.Profile()
#
#     def process_request(self, req, resp):
#         if self.profile:
#             self.profiler.clear()
#             self.profiler.enable()
#
#     def process_response(self, req, resp, resource, req_succeeded):
#         if self.profile:
#             self.profiler.disable()
#             s = io.StringIO()
#             sortby = 'time'
#             count = None
#             pstats.Stats(self.profiler, stream=s).sort_stats(sortby).print_stats(.6, count)
#             print(s.getvalue())


def init_error_log_handler(app, config, root):
    logger = logging.getLogger(root)

    handler = logging.StreamHandler()
    # handler.setLevel(config['LOG_STREAM_LEVEL'])
    # handler.setFormatter(logging.Formatter(config['LOG_STREAM_FORMAT']))
    logger.addHandler(handler)


def create_app():
    app = falcon.API(router=CIRouter())
    init_error_log_handler(app, {}, __name__)
    add_routes(app)
    return app


app = create_app()
