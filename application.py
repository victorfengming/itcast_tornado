import tornado.web
from views import index

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", index.IndexHandler),
            (r"/zhangmanyu", index.ZhangManYuHandler),



        ]
        super(Application, self).__init__(handlers)
