import os
import tornado.web
from views import index
from config import BASE_DIR, mysql


class Application(tornado.web.Application):
    def __init__(self, settings):
        handlers = [
            (r"/", index.IndexHandler),

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

        ]

        # 是不是傻了,这里直接就** 就行了
        super(Application, self).__init__(
            handlers,**settings
        )
