from tornado.web import RequestHandler
from tornado.web import StaticFileHandler
import tornado


# 设置静态默认
class MyStaticFileHandler(StaticFileHandler):
    # 我们用他的时候只需要重写他的init就可以了
    def __init__(self, *args, **kwargs):
        super(MyStaticFileHandler, self).__init__(*args, **kwargs)
        self.xsrf_token


# cookie
class PcookieHandler(RequestHandler):
    def get(self):
        # 设置cookie的方法
        self.set_cookie("suck", "wonderful")
        # 手动设置header中的cookie信息
        self.set_header("Set-Cookie", "kaige-nice; Path=/")

        self.write("cookie page info tornado!")


# cookie
class GetPCookieHandler(RequestHandler):
    def get(self):
        # 获取cookie
        # 那我们获取cookie是不是要通过cookie的名字来获取的啊
        # 要是没找到,那得有个默认值啊,
        # 我们一般情况下就是未登录的情况,这里设置成了未登录的
        cookie = self.get_cookie("suck", "未登录")
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
        self.set_secure_cookie("victor", "nice")
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
        count = self.get_cookie("count", "未登录")
        self.render("cookienum.html", count=count)


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


# 设置XsrfCookieHandler
class SetXsrfCookieHandler(RequestHandler):
    def get(self):
        # 设置一个_xsrf的cookie
        self.xsrf_token
        self.finish("OK")


'''登录页面'''
class LoginHandler(RequestHandler):
    def get(self):
        # 进入登录我就要知道我是从哪里进的了
        next = self.get_argument("next","/")
        url = "login" + "?next=" + next
        self.render("login.html", url=url)

    def post(self):
        '''
        咱也不用管是get还是post了
        name = self.get_body_argument("username")
        passwd = self.get_body_argument("passwd")
        '''
        # 直接我就写
        name = self.get_argument("username")
        passwd = self.get_argument("passwd")
        # TODO 这里还是把账号和密码写死了
        if name == "victor" and passwd == "123456":
            # 这个玩意代表从哪个页面跳来的,处理完了
            # 要是没毛病,我还得给你发到那里去
            next = self.get_argument("next", "/")
            # 后面"/"是默认值
            # 重定向走你,但是光重定向不行
            # 我们还得加一个标记
            self.redirect(next + "?flag=logined")
        else:
            next = self.get_argument("next", "/")
            '''
            # 验证失败了,
            # 路由的反向解析,听着挺高大上的
            # 密码输入错误,好几次也得记着人家是从哪里过来的
            '''
            log = self.reverse_url("login")+"?next="+next
            # 我还是得重定向
            self.redirect(log)

# 这个是主页面
class HomeHandler(RequestHandler):
    def get_current_user(self):
        '''
        # 返回True代表验证成功,否则凉凉
        # return False
        # 然后我们这里就能通过之前的flag来判断了
        # 这里还要设置一个默认值否则就是
        # WARNING:tornado.general:400 GET /home (127.0.0.1):
                  Missing argument flag
        '''
        flag = self.get_argument("flag", None)
        # 如果能取到flag,就返回true
        # 要是娶不到,自然就返回False
        return flag

    @tornado.web.authenticated
    def get(self):
        self.render("home.html")

# 这个cart是一个普通的页面
class CartHandler(RequestHandler):
    def get_current_user(self):
        return self.get_argument("flag", None)

    @tornado.web.authenticated
    def get(self):
        self.render("cart.html")
