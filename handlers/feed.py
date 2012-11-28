from tornado.web import asynchronous
from handlers.base import BaseHandler
import simplejson as json


class FeedHandler(BaseHandler):

    @asynchronous
    def get(self):
        get_questions = """SELECT * FROM `Question` LIMIT 10"""
        results = self.application.db.query(get_questions)
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(results))
        self.finish()
