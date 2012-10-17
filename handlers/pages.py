from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    """Handler to render index page"""

    def get(self):
        """Renders the index page"""
        self.render('index.html')


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
