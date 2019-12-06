import tornado.web
from views.index import IndexHandler

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler)
        ]
        super(Application,self).__init__(handlers)