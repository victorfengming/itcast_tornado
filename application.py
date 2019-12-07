import os
import tornado.web
from views import index
from config import BASE_DIR


class Application(tornado.web.Application):
    def __init__(self, settings):
        handlers = [
            (r"/", index.IndexHandler),
            # 渲染
            (r"/cart", index.CartHandler),

            # 数据库
            (r"/students", index.StudentsHandler),
            #
            # (
            #     r"/(.*)$",
            #     tornado.web.StaticFileHandler,
            #     {
            #         "path": os.path.join(BASE_DIR, "static/html"),
            #         "default_filename": "index.html"
            #     }
            #  ),



        ]

        super(Application, self).__init__(handlers, template_path=settings["template_path"],
                                          static_path=settings["static_path"])
