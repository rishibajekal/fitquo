import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler, asynchronous, authenticated
from tornado.auth import FacebookMixin
import simplejson as json

class SignupHandler(RequestHandler):
    @asynchronous
    def post(self):
        new_user = self.request.body
        user = json.loads(new_user)
        user_email = user['email']
        user_age = user['age']
        user_weight = user['weight']
        user_height = user['height']
        self.write(json.dumps(user))
        self.finish()