import tornado.web
from views import index

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", index.IndexHandler),
            (r"/sunck", index.SunckHandler,{'name':"victor",'age':19}),


            # 状态码
            (r"/status", index.StatusHandler),

        ]
        super(Application,self).__init__(handlers)