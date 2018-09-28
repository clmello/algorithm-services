from unittest.mock import patch
from unittest import TestCase

from tornado.testing import AsyncHTTPTestCase

from algorithm_services.app import make_app
from algorithm_services.app import MainHandler


class TestHelloApp(AsyncHTTPTestCase):

    def get_app(self):
        return make_app()

    def test_homepage(self):
        # response = self.fetch('/')
        self.http_client.fetch(self.get_url('/'), self.stop)
        response = self.wait()
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, b'Hello World')


class AppTestCase(TestCase):

    @patch('algorithm_services.app.Application')
    def test_make_app(self, application_mock):
        make_app()
        application_mock.assert_called_with(
            handlers=[(r"/", MainHandler)],
            debug=True,
            autoreload=True,
        )
