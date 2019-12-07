import tornado.web

import os
import config
from views import index

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            # (r'/', index.IndexHandler),

            #普通cookie
            (r'/pcookie', index.PCookieHandler),
            (r'/getpcookie', index.GetPCookieHandler),
            (r'/clearpcookie', index.ClearPCookieHandler),

            #安全cookie
            (r'/scookie', index.SCookieHandler),
            (r'/getscookie', index.GetSCookieHandler),


            #设置_xsrf的cookie
            (r'/setxsrfcookie', index.SetXSRFCookie),


            #cookie计数，记录浏览器访问次数
            (r'/cookienum', index.CookieNumHandler),
            (r'/postfile', index.PostFileHandler),



            #用户验证
            (r'/login', index.LoginHandler),
            (r'/home', index.HomeHandler),
            (r'/cart', index.CartHandler),


            (r'/(.*)$', index.StaticFileHandler, {"path":os.path.join(config.BASE_DIRS, "static/html"), "default_filename":"index.html"})

        ]
        super(Application,self).__init__(handlers, **config.settings)