import tornado.web
from tornado.web import RequestHandler

import json
import time

class StaticFileHandler(tornado.web.StaticFileHandler):
    def __init__(self, *args, **kwargs):
        super(StaticFileHandler, self).__init__(*args, **kwargs)
        self.xsrf_token

class Students1Handler(RequestHandler):
    def get(self):
        self.write("ok!!!!!!!!!")