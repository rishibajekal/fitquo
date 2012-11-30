import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.database
from tornado.web import RequestHandler, asynchronous
from tornado.auth import GoogleMixin
import simplejson as json


class GoogleLogin(RequestHandler, GoogleMixin):

    @asynchronous
    def get(self):
        if self.get_argument("openid.mode", None):
            self.get_authenticated_user(self.async_callback(self._on_auth))
            return
        self.authenticate_redirect()

    def _on_auth(self, user):
        if not user:
            raise tornado.web.HTTPError(500, "Google authentication failed. Please try again.")
        self.set_secure_cookie("fitquo", tornado.escape.json_encode(user))

        email = user['email']

        check_user_cmd = """SELECT `user_name` FROM `User` WHERE `user_email` = "%s" """ % email
        check_trainer_cmd = """SELECT `trainer_name` FROM `Trainer` WHERE `trainer_email` = "%s" """ % email

        user_result = self.application.db.query(check_user_cmd)
        trainer_result = self.application.db.query(check_trainer_cmd)

        # If user/trainer exists, go to the feed
        if len(user_result) != 0 or len(trainer_result) != 0:
            client = dict()
            if len(user_result) != 0:
                client["type"] = "user"
                self.set_secure_cookie("client_type", json.dumps(client))
            else:
                client["type"] = "trainer"
                self.set_secure_cookie("client_type", json.dumps(client))
            self.redirect('/profile')
        # If user does not exist, store in DB and go to pre signup
        else:
            self.redirect('/pre_signup')


class LogoutHandler(RequestHandler):

    @asynchronous
    def get(self):
        self.clear_cookie("fitquo")
        self.clear_cookie("client_type")
        self.redirect('/')
