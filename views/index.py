from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.write("main page info tornado!")


# cookie
class PcookieHandler(RequestHandler):
    def get(self):
        # 设置cookie的方法
        self.set_cookie("suck","wonderful")
        # 手动设置header中的cookie信息
        self.set_header("Set-Cookie","kaige-nice; Path=/")

        self.write("cookie page info tornado!")

