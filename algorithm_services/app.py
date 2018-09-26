import tornado.web


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('Hello')

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),])
