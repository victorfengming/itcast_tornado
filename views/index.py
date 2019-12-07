from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.write("main page info tornado!")
class HomeIndexHandler(RequestHandler):
    def get(self):

        def funcSum(a,b):
            return a + b

        self.render("home.html",func = funcSum)


class TranHandler(RequestHandler):
    def get(self):
        str = "<h1>能不能转义就看这会的了</h1>"
        self.render("trans.html",str = str)