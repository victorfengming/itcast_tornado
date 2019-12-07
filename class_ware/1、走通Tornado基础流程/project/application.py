import tornado.web

import os
import config
from views import index

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [


            (r'/(.*)$', index.StaticFileHandler,
             {"path": os.path.join(config.BASE_DIRS, "static/html"), "default_filename": "index.html"})
        ]
        super(Application,self).__init__(handlers, **config.settings)