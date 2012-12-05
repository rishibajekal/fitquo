from tornado.web import asynchronous
from handlers.base import BaseHandler
import simplejson as json


class UserInfoHandler(BaseHandler):

    @asynchronous
    def get(self, id=""):
        # Get user with email and write that JSON
        if (id == ""):
            curr_user = json.loads(self.get_current_user())
            get_user = """SELECT * FROM `User` WHERE `user_email` = "%s" """\
                            % (curr_user['email'])
        else:
            curr_id = id
            get_user = """SELECT * FROM `User` WHERE `user_id` = "%s" """\
                % (curr_id)

        user = self.application.db.get(get_user)
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(user))
        self.finish()


class UserSignupHandler(BaseHandler):

    @asynchronous
    def post(self):
        curr_user = json.loads(self.get_current_user())
        name = curr_user["name"]
        email = curr_user["email"]

        body = json.loads(self.request.body)
        user = body["user"]
        user["name"] = name
        user["email"] = email
        if self.add_user(user):
            self.write({"success": "true"})
        else:
            self.write({"success": "false"})
        self.finish()

    def add_user(self, user):
        add_user_info = """INSERT INTO `User` (`user_name`, `user_email`, `age`, `weight`, `height`) VALUES ("%s", "%s", %d, %d, %d)"""\
                        % (user["name"], user["email"], user["age"], user["weight"], user["height"])
        result = self.application.db.execute(add_user_info)
        select_user_id = """SELECT `user_id` FROM `User` WHERE `user_email`="%s" """\
                    % (user["email"])
        result = self.application.db.get(select_user_id)
        user_id = int(result["user_id"])

        for topic_name in user["interests"]:
            select_topic_id = """SELECT `topic_id` FROM `FitnessTopics` WHERE `name`="%s" """\
                        % (topic_name)
            topic_id = self.application.db.get(select_topic_id)
            add_interests = """INSERT INTO `Interests` (`user_id`, `topic_id`) VALUES (%d, %d)"""\
                % (user_id, topic_id['topic_id'])
            result = self.application.db.execute(add_interests)

        return True if result is not None else False
