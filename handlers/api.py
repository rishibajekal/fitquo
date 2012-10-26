from tornado.web import asynchronous
from handlers.base import BaseHandler
import simplejson as json


class SignupHandler(BaseHandler):

    @asynchronous
    def post(self):
        new_user = self.request.body
        user = json.loads(new_user)

        user_age = int(user['age'])
        user_weight = int(user['weight'])
        user_height = int(user['height'])

        curr_user = json.loads(self.get_current_user())

        add_user_info = """UPDATE `User` SET `age`=%d, `weight`=%d, `height`=%d WHERE `user_email` = "%s" """\
                        % (user_age, user_weight, user_height, curr_user['email'])
        self.application.db.execute(add_user_info)

        self.write(json.dumps(user))
        self.finish()


class UserHandler(BaseHandler):

    def get(self):
        # Get user with email and write that JSON
        curr_user = json.loads(self.get_current_user())

        get_user = """SELECT * FROM `User` WHERE `user_email` = "%s" """\
                        % (curr_user['email'])
        user = self.application.db.query(get_user)[0]
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(user))
        self.finish()
