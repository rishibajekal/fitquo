from tornado.web import authenticated
from handlers.base import BaseHandler
import simplejson as json


class IndexPageHandler(BaseHandler):

    def get(self):
        self.renderPage('index.html')


class AboutPageHandler(BaseHandler):

    def get(self):
        self.renderPage("about.html")


class ContactPageHandler(BaseHandler):

    def get(self):
        self.renderPage("contact.html")


class ProfilePageHandler(BaseHandler):

    @authenticated
    def get(self, id=None):

        if(id == None):
            client = json.loads(self.get_client_type())
            if client['type'] == 'user':
                self.renderPage("user_profile.html", user_id="")
            else:
                self.renderPage("trainer_profile.html")
        else:
            self.renderPage("user_profile.html", user_id=id)


class PreSignupPageHandler(BaseHandler):

    @authenticated
    def get(self):
        self.renderPage("pre_signup.html")


class UserSignupPageHandler(BaseHandler):

    @authenticated
    def get(self):
        client = dict()
        client["type"] = "user"
        self.set_secure_cookie("client_type", json.dumps(client))
        self.renderPage("user_signup.html")


class TrainerSignupPageHandler(BaseHandler):

    @authenticated
    def get(self):
        client = dict()
        client["type"] = "trainer"
        self.set_secure_cookie("client_type", json.dumps(client))
        self.renderPage("trainer_signup.html")


class QuestionPageHandler(BaseHandler):

    @authenticated
    def get(self):
        self.renderPage("ask.html")


class FeedPageHandler(BaseHandler):

    @authenticated
    def get(self):
        self.renderPage("feed.html")


class SearchPageHandler(BaseHandler):

    @authenticated
    def get(self):
        self.renderPage("search.html")


class AnswerPageHandler(BaseHandler):

    @authenticated
    def get(self, id):
        self.renderPage("answers.html", question_id=id)


class RecommendPageHandler(BaseHandler):

    @authenticated
    def get(self):
        self.renderPage("recommend.html")
