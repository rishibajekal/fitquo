from tornado.web import asynchronous
from handlers.base import BaseHandler
import simplejson as json


class SignupHandler(BaseHandler):

    @asynchronous
    def post(self):
        new_user = self.request.body
        user = json.loads(new_user)

        user_email = user['email']
        user_age = int(user['age'])
        user_weight = int(user['weight'])
        user_height = int(user['height'])

        curr_user = json.loads(self.get_current_user())

        add_user_info = """UPDATE `User` SET `user_email`="%s", `age`=%d, `weight`=%d, `height`=%d WHERE `fb_id` = %d"""\
                        % (user_email, user_age, user_weight, user_height, curr_user['uid'])
        self.application.db.execute(add_user_info)

        self.write(json.dumps(user))
        self.finish()


class UserHandler(BaseHandler):

    def get(self, fb_id):
        # FIXME
        # Get user with Facebook ID and write that JSON
        self.write("{'name': 'Rishi Bajekal', 'email': 'rishi.bajekal@gmail.com', 'fb_id':"
            + fb_id + "}")
        self.finish()
