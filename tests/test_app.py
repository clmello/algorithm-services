from tornado.testing import AsyncHTTPTestCase
from algorithm_services import app


class TestHelloApp(AsyncHTTPTestCase):

    def get_app(self):
        return app.make_app()

    def test_homepage(self):
        # response = self.fetch('/')
        self.http_client.fetch(self.get_url('/'), self.stop)
        response = self.wait()
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, b'Hello')
