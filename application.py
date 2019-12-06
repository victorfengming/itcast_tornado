import tornado.web
from views import index

class Application(tornado.web.Application):
    def __init__(self,settings):
        handlers = [
            (r"/", index.IndexHandler),

            # 上传文件
            tornado.web.url(r"/upfile", index.UpFileHandler),

        ]


        super(Application, self).__init__(handlers,template_path=settings["template_path"])
