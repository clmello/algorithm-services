from unittest.mock import patch
from unittest import TestCase

from tornado.testing import AsyncHTTPTestCase

from algorithm_services.app import make_app
from algorithm_services.app import MainHandler
from algorithm_services.options import get_options


class TestHelloApp(AsyncHTTPTestCase):

    def get_app(self):
        options = get_options('local')
        return make_app(options)

    def test_homepage(self):
        # response = self.fetch('/')
        self.http_client.fetch(self.get_url('/'), self.stop)
        response = self.wait()
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, b'Hello World')


class AppTestCase(TestCase):

    @patch('algorithm_services.app.Application')
    def test_make_app(self, application_mock):
        options = get_options('local')
        make_app(options)
        application_mock.assert_called_with(
            handlers=[(r"/", MainHandler)],
            debug=True,
            autoreload=True,
        )


class OptionTestCase(TestCase):

    @patch('algorithm_services.options.options')
    @patch('algorithm_services.options.parse_config_file')
    def test_get_options(self, parse_mock, options_mock):
        options = get_options('local')
        parse_mock.assert_called_with('./algorithm_services/config/local.conf')
        self.assertEqual(options, options_mock)
