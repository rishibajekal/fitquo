import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.database
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

        pic_url = user['pic_square']
        name = user['name']
        fb_id = user['uid']

        check_user_cmd = """SELECT `user_name` FROM `User` WHERE `fb_id` = %d""" % fb_id

        result = self.application.db.query(check_user_cmd)
        # If user does not exist, store in DB and go to signup
        if len(result) == 0:
            add_user = """INSERT INTO `User` (`fb_id`, `user_name`, `pic_url`) VALUES (%d, "%s", "%s")"""\
                        % (fb_id, name, pic_url)
            self.application.db.execute(add_user)
            self.redirect('/signup')
        # If user exists, go to their profile
        else:
            # self.redirect('/feed')
            self.redirect('/profile')
