from tornado.web import Application
from tornado.web import RequestHandler


class MainHandler(RequestHandler):

    def get(self):
        self.write('Hello World')


def make_app():
    return Application(
        handlers=[(r"/", MainHandler)],
        debug=True,
        autoreload=True,
    )
