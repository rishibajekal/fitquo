from tornado.web import asynchronous
from handlers.base import BaseHandler
import simplejson as json


class SearchHandler(BaseHandler):

    @asynchronous
    def post(self):
        search_body = json.loads(self.request.body)
        search_query = search_body["search"]
        if(search_query["advanced"] == "no"):
            self.simple(search_query)
        else:
            self.advanced(search_query)
        self.finish()

    def simple(self, data):
        search_content = data["content"]

        get_id_request = "SELECT question_id FROM Question WHERE content LIKE %s"
        search_string = "%" + search_content + "%"
        param = (search_string)
        results = self.application.db.query(get_id_request, param)
        self.get_questions(results)

    def advanced(self, data):
        print "advanced"

    def get_questions(self, question_identifiers):
        search_results = []
        for question in question_identifiers:
            get_question = "SELECT content FROM Question WHERE question_id = %s"
            question_id = (question['question_id'])
            query_result = self.application.db.get(get_question, question_id)
            result = {}
            result["content"] = query_result["content"]
            result["id"] = question_id
            search_results.append(result)
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(search_results))
