import tornado.web
from tornado.web import RequestHandler
import simplejson as json


class BaseHandler(RequestHandler):
    """BaseHandler for RequestHandlers to inherit from"""

    def get_current_user(self):
        user = self.get_secure_cookie("fitquo")
        return user

    def get_client_type(self):
        client = self.get_secure_cookie("client_type")
        return client

    def check_xsrf_cookie(self):
        token = (self.get_argument("_xsrf", None) or
                (json.loads(self.request.body)["_xsrf"]))
        if not token:
            raise tornado.web.HTTPError(403, "'_xsrf' argument missing from POST")
        if self.xsrf_token != token:
            raise tornado.web.HTTPError(403, "XSRF cookie does not match POST argument")
