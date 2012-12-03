from tornado.web import asynchronous
from handlers.base import BaseHandler
import simplejson as json


class RecommendHandler(BaseHandler):

    @asynchronous
    def get(self):
        curr_user = json.loads(self.get_current_user())

        user_email = curr_user['email']
        select_user_id = """SELECT `user_id` FROM `User` WHERE `user_email`="%s" """\
                    % (user_email)
        result = self.application.db.get(select_user_id)
        user_id = result["user_id"]

        get_trainers = "SELECT * FROM Trainer WHERE trainer_id IN\
                        (SELECT DISTINCT(SpecializesIn.trainer_id)\
                        FROM SpecializesIn\
                        INNER JOIN Interests\
                        ON SpecializesIn.topic_id=Interests.topic_id\
                        AND Interests.user_id=%s)"
        results = self.application.db.query(get_trainers, (user_id))

        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(results))
        self.finish()
