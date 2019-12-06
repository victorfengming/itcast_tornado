import tornado.web
from views import index

class Application(tornado.web.Application):
    def __init__(self,settings):
        handlers = [
            (r"/", index.IndexHandler),



            # request对象
            tornado.web.url(r"/zhuyin", index.ZhuYinHandler),

        ]


        super(Application, self).__init__(handlers,template_path=settings["template_path"])
