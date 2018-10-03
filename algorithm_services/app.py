from tornado.web import Application
from tornado.web import RequestHandler

from algorithm_services.handlers import MainHandler


def make_app(options):
    return Application(
        handlers=[(r"/", MainHandler)],
        debug=options.debug,
        autoreload=options.autoreload,
    )
