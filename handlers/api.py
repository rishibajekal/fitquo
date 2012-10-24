from tornado.web import asynchronous
from handlers.base import BaseHandler
import simplejson as json


class SignupHandler(BaseHandler):

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


class UserHandler(BaseHandler):

    def get(self, fb_id):
        # FIXME
        # Get user with Facebook ID and write that JSON
        self.write("{'name': 'Rishi Bajekal', 'email': 'rishi.bajekal@gmail.com', 'fb_id':"
            + fb_id + "}")
        self.finish()
