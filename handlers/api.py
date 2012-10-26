from tornado.web import asynchronous
from handlers.base import BaseHandler
import simplejson as json


# REMOVE ME FOR REAL CODE (USE SOME FOR LOGOUT)
class DeleteUserHandler(BaseHandler):

    @asynchronous
    def get(self):
        curr_user = json.loads(self.get_current_user())
        delete_user = """DELETE FROM `User` WHERE `user_email` = "%s" """\
                        % (curr_user['email'])
        self.application.db.execute(delete_user)
        self.clear_cookie("fitquo")
        self.write('{"deleted": "true"}')
        self.finish()


class UserSearchHandler(BaseHandler):

    @asynchronous
    def get(self):
        # Get the search content from the client
        user_search_body = self.request.body
        user_search = json.loads(user_search_body)

        # Do the SQL command to search for given user
        sql = """SELECT `user_name`, `user_id` FROM `User` WHERE `user_name` = "%s" """\
                % (user_search['query'])
        rows = self.application.db.query(sql)

        print json.dumps(rows)

        # send resulting json back to client-side
        #self.set_header("Content-Type", "application/json")
        #self.write(json.dumps(rows))
        self.finish()


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
