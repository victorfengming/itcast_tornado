
import tornado.ioloop
import tornado.httpserver
import tornado.options

import config
from application import Application


if __name__ == '__main__':
    app = Application(config.settings)
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.bind(config.options["port"])
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()
