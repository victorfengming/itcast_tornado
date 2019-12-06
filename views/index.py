from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.write("main page info tornado!")

class HomeHandler(RequestHandler):
    def get(self):
        self.write(" this is home page content!")
