from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.write("main page info tornado!")
