import tornado.web
from views import index

class Application(tornado.web.Application):
    def __init__(self,settings):

        handlers = [
            (r"/", index.IndexHandler),
            # 渲染
            (r"/home", index.HomeIndexHandler),

        ]

        super(Application, self).__init__(handlers,template_path=settings["template_path"],static_path=settings["static_path"])
