from tornado.web import asynchronous
from handlers.base import BaseHandler
import simplejson as json


class AnswerHandler(BaseHandler):

    @asynchronous
    def post(self):
        curr_user = json.loads(self.get_current_user())

        trainer_email = curr_user['email']
        select_trainer_id = """SELECT `trainer_id` FROM `Trainer` WHERE `trainer_email`="%s" """\
                    % (trainer_email)
        result = self.application.db.get(select_trainer_id)
        trainer_id = int(result["trainer_id"])

        body = json.loads(self.request.body)
        new_answer = body["answer"]
        answer_content = new_answer['content']
        answer_time = new_answer['timestamp']
        related_question = int(new_answer['question_id'])

        add_answer = """INSERT INTO `Answer` (`trainer_id`, `content`, `posted_at`, `question_id`) VALUES (%d, "%s","%s", %d)"""\
            % (trainer_id, answer_content, answer_time, related_question)
        self.application.db.execute(add_answer)
        self.finish()


class DeleteAnswerHandler(BaseHandler):

    @asynchronous
    def post(self):
        body = json.loads(self.request.body)
        answer_id = body["id"]
        delete_answer = "DELETE FROM Answer WHERE answer_id=%s"
        self.application.db.execute(delete_answer, (answer_id))
        self.finish()
