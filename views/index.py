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
# cookie
class GetPCookieHandler(RequestHandler):
    def get(self):
        # 获取cookie
        # 那我们获取cookie是不是要通过cookie的名字来获取的啊
        # 要是没找到,那得有个默认值啊,
        # 我们一般情况下就是未登录的情况,这里设置成了未登录的
        cookie = self.get_cookie("suck","未登录")
        print(cookie)
        self.write("getcookie page info tornado!")
        self.write(cookie)

