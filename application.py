import tornado.web
from views import index

class Application(tornado.web.Application):
    def __init__(self,settings):
        handlers = [
            (r"/", index.IndexHandler),


            # POST
            tornado.web.url(r"/postfile", index.PostfileHandler, name='postfile'),

        ]


        super(Application, self).__init__(handlers,template_path=settings["template_path"])
