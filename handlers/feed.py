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


class QuestionAnswerHandler(BaseHandler):

    @asynchronous
    def get(self, id):
        get_question = """SELECT * FROM `Question` WHERE `question_id` = "%s" """\
                        % (id)
        get_answers = """SELECT * FROM `Answer` WHERE `question_id` = "%s" LIMIT 10"""\
                        % (id)

        question = self.application.db.query(get_question)
        answers = self.application.db.query(get_answers)

        print question
        print answers

        self.finish()
