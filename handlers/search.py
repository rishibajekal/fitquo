from tornado.web import asynchronous
from handlers.base import BaseHandler
import simplejson as json
import pq
import string


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
        question_identifiers = []
        for result in results:
            question_id = result["question_id"]
            question_identifiers.append(question_id)
        self.get_questions(question_identifiers)

    def advanced(self, data):
        p = pq.PriorityQueue()
        counter = 0
        question_identifiers = []
        search_content = data["content"]
        wordsmod = search_content.translate(None, string.punctuation)
        words = wordsmod.lower().split()
        for word in words:
            counter += 1
            sets = self.application.r_server.smembers(word)
            for i in sets:
                p.insert(i)
        while(p.empty() == False):
            question_identifiers.append(p.popper())

        self.get_questions(question_identifiers)

    def get_questions(self, question_identifiers):
        search_results = []
        for question in question_identifiers:
            get_question = "SELECT content FROM Question WHERE question_id = %s"
            #question_id = (question['question_id'])
            query_result = self.application.db.get(get_question, question)
            result = {}
            result["content"] = query_result["content"]
            result["id"] = question
            search_results.append(result)
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(search_results))
