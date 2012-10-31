from tornado.web import asynchronous
from handlers.base import BaseHandler
import simplejson as json


class UserHandler(BaseHandler):

    @asynchronous
    def get(self):
        # Get user with email and write that JSON
        curr_user = json.loads(self.get_current_user())

        get_user = """SELECT * FROM `User` WHERE `user_email` = "%s" """\
                        % (curr_user['email'])
        user = self.application.db.get(get_user)
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(user))
        self.finish()


class SignupHandler(BaseHandler):

    @asynchronous
    def post(self):
        body = json.loads(self.request.body)
        user = body["user"]

        if self.add_user(user):
            self.write({"success": "true"})
        else:
            self.write({"success": "false"})
        self.finish()

    def add_user(self, user):
        curr_user = json.loads(self.get_current_user())

        add_user_info = """UPDATE `User` SET `age`=%d, `weight`=%d, `height`=%d WHERE `user_email` = "%s" """\
                        % (user["age"], user["weight"], user["height"], curr_user["email"])
        result = self.application.db.execute(add_user_info)

        return True if result is not None else False
