import os

from tornado.httpserver import HTTPServer
import tornado.ioloop

from app import make_app
from options import get_options


def main(options):
    app = make_app(options)
    server = HTTPServer(app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    options = get_options(os.environ.get('ENV', 'local'))
    main(options)
