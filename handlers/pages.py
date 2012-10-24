from tornado.web import authenticated
from handlers.base import BaseHandler


class IndexPageHandler(BaseHandler):
    """Handler to render index page"""

    def get(self):
        self.render('out_index.html')


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
        self.render("profile.html")


class SignupPageHandler(BaseHandler):
    """Handler to render signup page"""

    @authenticated
    def get(self):
        self.render("user_signup.html")
