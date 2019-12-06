from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.write("main page info tornado!")
class HomeIndexHandler(RequestHandler):
    def get(self):
        temp = 100
        # 直接传一个变量就行
        self.render("home.html",num = temp)
        # self.render("home.html")
