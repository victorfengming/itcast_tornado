import os
import tornado.web
from views import index
from config import BASE_DIR, mysql


class Application(tornado.web.Application):
    def __init__(self, settings):

        handlers = [
            # (r"/", index.IndexHandler),

            # 普通cookie
            (r"/pcookie", index.PcookieHandler),
            # 获取cookie
            (r"/getpcookie", index.GetPCookieHandler),
            # 清除cookie
            (r"/clearpcookie", index.ClearPCookieHandler),
            # 安全cookie
            (r"/scookie", index.SCookieHandler),
            # 获取安全cookie
            (r"/getscookie", index.GetSCookieHandler),
            # cookie计数,记录浏览器访问次数
            (r"/cookienum", index.CookieNumHandler),
            # postfile
            (r"/postfile", index.PostFileHandler),
            # 设置_xsrfcookie
            (r"/setxsrfcookie", index.SetXsrfCookieHandler),

            # 登录界面
            tornado.web.url(r"/login", index.LoginHandler,name='login'),
            # home页面
            (r"/home", index.HomeHandler),
            (r"/cart", index.CartHandler),

            (
                r"/(.*)$",
                # 系统这个我们不能用,所以我们继承,
                # tornado.web.StaticFileHandler,
                # 让我们自己写这个继承自系统给我们这个
                index.MyStaticFileHandler,
                {
                    "path": os.path.join(BASE_DIR, "static/html"),
                    "default_filename": "index.html"
                }
            ),

        ]
        # 是不是傻了,这里直接就** 就行了
        super(Application, self).__init__(
            handlers,**settings
        )
