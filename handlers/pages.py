from tornado.web import RequestHandler, authenticated


class IndexHandler(RequestHandler):
    """Handler to render index page"""

    def get(self):
        """Renders the index page"""
        self.render('out-index.html')


class AboutHandler(RequestHandler):
    """Handler to render about page"""

    def get(self):
        """Renders the about page"""
        self.render("about.html")


class ContactHandler(RequestHandler):
    """Handler to render contact page"""

    def get(self):
        """Renders the contact page"""
        self.render("contact.html")


class ProfileHandler(RequestHandler):
    """Handler to render profile page"""

    @authenticated
    def get(self):
        """Renders the profile page"""
        self.render("profile.html")


class SignupHandler(RequestHandler):
    """Handler to render signup page"""

    @authenticated
    def get(self):
        """Renders the signup page"""
        self.render("user-signup.html")
