import tornado.web
from views import index

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", index.IndexHandler),
            (r"/sunck", index.SunckHandler,{'name':"victor",'age':19}),


            # 状态码
            (r"/status", index.StatusHandler),
            # 重定向
            (r"/index", index.RedirectHandler),
            # 错误处理
            # iserror?flag=2
            # 如果等于0就说明,有错误,不等于0就说明没有错误
            (r"/iserror", index.ErrorHandler),

            tornado.web.url(r"/kaige",index.KaigeHandler,name='kaige'),
        ]
        super(Application,self).__init__(handlers)