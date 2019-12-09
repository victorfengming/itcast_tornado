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

# 清除cookie
class ClearPCookieHandler(RequestHandler):
    def get(self):
        # 这个删除cookie后,他这次不能决定
        # 是下一次删除了
        # 清除一个cookie
        self.clear_cookie("suck")
        # 清除所有cookie
        self.clear_all_cookies()
        self.write("ClearPCookieHandler page info tornado!")

# 安全cookie
class SCookieHandler(RequestHandler):
    def get(self):
        self.set_secure_cookie("victor","nice")
        self.write("SCookieHandler page info tornado!")

# 获取安全cookie
class GetSCookieHandler(RequestHandler):
    def get(self):
        sc = self.get_secure_cookie("victor")
        print(sc)
        self.write("getSCookieHandler page info tornado!")
        self.write(sc)


# cookie计数
class CookieNumHandler(RequestHandler):
    def get(self):

        count = self.get_cookie("count","未登录")
        self.render("cookienum.html",count = count)

# PostFileHandler 用于这个那个
class PostFileHandler(RequestHandler):
    def get(self):
        self.render("postfile.html")

    def post(self):
        count = self.get_cookie("count", None)
        if count:
            # 第n次访问
            count = str(int(count) + 1)
            pass
        else:
            # 第一次访问
            # 设置cookie
            count = '0'
        self.set_cookie("count", count)
        self.redirect("/cookienum")
