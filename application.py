import tornado.web
from views import index

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", index.IndexHandler),

            # (r"/good/(\w+)/(\w+)/(\w+)", index.GoodHandler),
            (r"/good/(?P<p1>\w+)/(?P<p3>\w+)/(?P<p2>\w+)", index.GoodHandler),

        ]
        super(Application, self).__init__(handlers)
