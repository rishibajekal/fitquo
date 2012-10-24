import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler, asynchronous
from tornado.auth import FacebookMixin


class FacebookLogin(RequestHandler, FacebookMixin):
    @asynchronous
    def get(self):
        if self.get_argument("session", None):
            self.get_authenticated_user(self.async_callback(self._on_auth))
            return
        self.authenticate_redirect()

    def _on_auth(self, user):
        if not user:
            raise tornado.web.HTTPError(500, "Facebook authentication failed. Please try again.")
        self.set_secure_cookie("fitquo", tornado.escape.json_encode(user))

        username = user['username']
        pic_url = user['pic_square']
        name = user['name']
        uid = user['uid']

        # TODO: We should query database based on current user
        # if (user exists in db): render profile.html
        # else: put values in db and go to signup.html

        self.redirect('/signup')
