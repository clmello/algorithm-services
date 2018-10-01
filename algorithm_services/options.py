from tornado.options import define
from tornado.options import options
from tornado.options import parse_config_file


define('port', default=8080, help='port to listen on')
define('autoreload', default=False, type=bool, help='enable autoreload')
define('debug', default=False, type=bool, help='enable debug')


def get_options(env):
    parse_config_file('./algorithm_services/config/{env}.conf'.format(
        env=env,
    ))
    return options
