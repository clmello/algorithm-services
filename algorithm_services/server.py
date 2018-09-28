from tornado.httpserver import HTTPServer
import tornado.ioloop

from app import make_app


def main():
    app = make_app()
    server = HTTPServer(app)
    server.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
