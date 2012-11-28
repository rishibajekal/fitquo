from tornado.web import authenticated
from handlers.base import BaseHandler
import simplejson as json


class IndexPageHandler(BaseHandler):
    """Handler to render index page"""

    def get(self):
        self.render('index.html')


class AboutPageHandler(BaseHandler):
    """Handler to render about page"""

    def get(self):
        self.render("about.html")


class ContactPageHandler(BaseHandler):
    """Handler to render contact page"""

    def get(self):
        self.render("contact.html")


class ProfilePageHandler(BaseHandler):
    """Handler to render profile page"""

    @authenticated
    def get(self):
        client = json.loads(self.get_client_type())
        if client['type'] == 'user':
            self.render("user_profile.html")
        else:
            self.render("trainer_profile.html")


class PreSignupPageHandler(BaseHandler):
    """Handler to render the pre signup page"""

    @authenticated
    def get(self):
        self.render("pre_signup.html")


class UserSignupPageHandler(BaseHandler):
    """Handler to render user signup page"""

    @authenticated
    def get(self):
        client = dict()
        client["type"] = "user"
        self.set_secure_cookie("client_type", json.dumps(client))
        self.render("user_signup.html")


class TrainerSignupPageHandler(BaseHandler):
    """Handler to render trainer signup page"""

    @authenticated
    def get(self):
        client = dict()
        client["type"] = "trainer"
        self.set_secure_cookie("client_type", json.dumps(client))
        self.render("trainer_signup.html")


class QuestionPageHandler(BaseHandler):
    """Handler to render page to ask a question"""

    @authenticated
    def get(self):
        self.render("ask.html")


class FeedPageHandler(BaseHandler):
    """Handler to render feed page"""

    @authenticated
    def get(self):
        self.render("feed.html")
