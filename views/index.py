from typing import Any

from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.write("main page info tornado!")







class ZhuYinHandler(RequestHandler):

    def get(self):
        print(self.request)
