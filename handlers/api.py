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
        # FIXME
        # Get user with email and write that JSON
        #self.set_header("Content-Type", "application/json")
        user = {'name': "Rishi", 'email': "rishi.bajekal@gmail.com", 'age': "20", 'weight': "75", 'height': "5ft8"}
        self.write(json.dumps(user))
        self.finish()
