from tornado.web import asynchronous
from handlers.base import BaseHandler
import simplejson as json


class QuestionHandler(BaseHandler):

    @asynchronous
    def post(self):
        curr_user = json.loads(self.get_current_user())

        user_email = curr_user['email']
        select_user_id = """SELECT `user_id` FROM `User` WHERE `user_email`="%s" """\
                    % (user_email)
        result = self.application.db.get(select_user_id)
        user_id = int(result["user_id"])

        body = json.loads(self.request.body)
        new_question = body["question"]
        question_content = new_question['content']
        question_time = new_question['timestamp']
        add_question = """INSERT INTO `Question` (`user_id`, `content`, `posted_at`) VALUES (%d, "%s","%s")"""\
            % (user_id, question_content, question_time)
        self.application.db.execute(add_question)
        self.finish()


class QuestionAnswerHandler(BaseHandler):

    @asynchronous
    def get(self, id):
        get_question = """SELECT * FROM `Question` WHERE `question_id` = "%s" """\
                        % (id)
        get_answers = """SELECT * FROM `Answer` WHERE `question_id` = "%s" LIMIT 10"""\
                        % (id)

        question = self.application.db.get(get_question)
        answers = self.application.db.query(get_answers)

        list = []
        list.append(question)
        list.append(answers)

        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(list))
        self.finish()
