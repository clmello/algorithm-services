from tornado.web import Application
from tornado.web import RequestHandler


class MainHandler(RequestHandler):

    def get(self):
        self.write('Hello World')


def make_app(options):
    return Application(
        handlers=[(r"/", MainHandler)],
        debug=options.debug,
        autoreload=options.autoreload,
    )
