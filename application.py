import os
import tornado.web
from views import index
from config import BASE_DIR, mysql



class Application(tornado.web.Application):
    def __init__(self, settings):
        handlers = [
            (r"/", index.IndexHandler),

            # 普通cookie
            (r"/pcookie", index.PcookieHandler),

        ]

        super(Application, self).__init__(
            handlers,
            template_path=settings["template_path"],
            static_path=settings["static_path"]
        )
