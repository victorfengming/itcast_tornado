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

        ]

        super(Application, self).__init__(
            handlers,
            # 模板路径
            template_path=settings["template_path"],
            # 静态路径
            static_path=settings["static_path"],
            # cookie签名
            cookie_secret=settings["cookie_secret"],
        )
