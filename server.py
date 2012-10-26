import os
import sys
import logging
import tornado.database
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options, define
from handlers.pages import *
from handlers.login import *
from handlers.api import *

PORT = sys.argv[1]

define("port", default=PORT, help="run on the given port", type=int)
define("debug", default=False, help="run tornado in debug mode", type=bool)
define("mysql_host", default="localhost:3306", help="host and port mysql is running on")
define("mysql_database", default="fitquo", help="name of the mysql database")
define("mysql_user", default="root", help="name of the mysql user")
define("mysql_password", default="", help="password of the mysql user")


class Application(tornado.web.Application):
    """The main application class for Fitquo"""

    def __init__(self):
        """Creates the application with specified settings"""

        self.db = tornado.database.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)

        handlers = [

            # Page Handlers
            tornado.web.URLSpec(r'/', IndexPageHandler),
            tornado.web.URLSpec(r'/about', AboutPageHandler),
            tornado.web.URLSpec(r'/contact', ContactPageHandler),
            tornado.web.URLSpec(r'/profile', ProfilePageHandler),
            tornado.web.URLSpec(r'/signup', SignupPageHandler),

            # API Handlers

            # DELETE ME (CHANGE TO LOGOUT)
            tornado.web.URLSpec(r'/api/delete', DeleteUserHandler),
            tornado.web.URLSpec(r'/query_results', QueryResultsHandler),

            tornado.web.URLSpec(r'/api/search', UserSearchHandler),
            tornado.web.URLSpec(r'/api/signup', SignupHandler),
            tornado.web.URLSpec(r'/api/user', UserHandler),
            tornado.web.URLSpec(r'/login', GoogleLogin)
        ]

        current_dir = os.path.dirname(__file__)

        settings = dict(
            template_path=os.path.join(current_dir, 'templates'),
            static_path=os.path.join(current_dir, 'static'),
            login_url='/login',
            debug=options.debug,
            autoescape='xhtml_escape',
            cookie_secret='947e5d1dc624bc99421bfc7e8ebad245',
        )

        super(Application, self).__init__(handlers, **settings)

        logging.info('Server started on port {0}'.format(options.port))

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
