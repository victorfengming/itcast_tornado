import tornado.web

import os
from config import settings,BASE_DIRS
from views import index

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [

            (r'/students1', index.Students1Handler),
            (r'/students2', index.Students2Handler),
            (r'/students3', index.Students3Handler),
            (r'/home', index.HomeHandler),

            (r'/(.*)$', index.StaticFileHandler,
             {"path": os.path.join(BASE_DIRS, "static/html"), "default_filename": "index.html"})
        ]
        super(Application,self).__init__(handlers, **settings)