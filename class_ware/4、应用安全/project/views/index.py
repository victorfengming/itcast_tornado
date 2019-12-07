import tornado.web
from tornado.web import RequestHandler

# class IndexHandler(RequestHandler):
#     def get(self, *args, **kwargs):
#         self.write("sunck is a good man")
class StaticFileHandler(tornado.web.StaticFileHandler):
    def __init__(self, *args, **kwargs):
        super(StaticFileHandler, self).__init__(*args, **kwargs)
        self.xsrf_token

#cookie
class PCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        #设置
        self.set_cookie("sunck","good")
        # self.set_header("Set-Cookie","kaige=nice; Path=/")
        self.write("ok")
class GetPCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        #获取cookie
        cookie = self.get_cookie("sunck", "未登录")
        print("cookie =", cookie)
        self.write("ok")
class ClearPCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        #清除一个cookie
        # self.clear_cookie("sunck")
        #清除所有cookie
        self.clear_all_cookies()
        self.write("ok")



#安全cookie
class SCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.set_secure_cookie("zhangmanyu","nice")
        self.write("ok")
class GetSCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        scookie = self.get_secure_cookie("zhangmanyu")
        print("scookie =", scookie)
        self.write("ok")


#cookie计数
class CookieNumHandler(RequestHandler):
    def get(self, *args, **kwargs):
        count = self.get_cookie("count","未登录")
        self.render('cookienum.html', count = count)

class PostFileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('postfile.html')
    def post(self, *args, **kwargs):
        count = self.get_cookie("count", None)
        if not count:
            count = 1
        else:
            count = int(count)
            count += 1
        self.set_cookie("count", str(count))
        self.redirect("/cookienum")



class SetXSRFCookie(RequestHandler):
    def get(self, *args, **kwargs):
        #设置_xsrf的cookie
        self.xsrf_token
        self.finish("Ok")






#用户验证
class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        next = self.get_argument("next", "/")
        url = "login?next=" + next
        self.render("login.html", url = url)
    def post(self, *args, **kwargs):
        name = self.get_argument("username")
        pawd = self.get_argument("passwd")
        if name == "1" and pawd == "1":
            next = self.get_argument("next", "/")
            self.redirect(next+"?flag=logined")
        else:
            next = self.get_argument("next", "/")
            print("next = ", next)
            self.redirect("/login?next="+next)
class HomeHandler(RequestHandler):
    def get_current_user(self):
        #  /home
        flag = self.get_argument("flag", None)
        return flag
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("home.html")
class CartHandler(RequestHandler):
    def get_current_user(self):
        #  /home
        flag = self.get_argument("flag", None)
        return flag
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("cart.html")
