from tornado.web import asynchronous
from handlers.base import BaseHandler
import simplejson as json


class FeedHandler(BaseHandler):

    @asynchronous
    def get(self):
        get_questions = """SELECT * FROM `Question`"""
        results = self.application.db.query(get_questions)
        self.set_header("Content-Type", "application/json")
        for result in results:
            user_id = result['user_id']
            get_user = "SELECT user_name FROM User WHERE user_id = %s"
            user = self.application.db.get(get_user, (user_id))
            user_name = user['user_name']
            result["author"] = user_name
        self.write(json.dumps(results))
        self.finish()
