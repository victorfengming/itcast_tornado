import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

#定义两个参数
tornado.options.define("port",default=8000,type=int)
tornado.options.define("list",default=[],type=str,multiple=True)

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("sunck is a good man")

if __name__ == "__main__":
    # 转换命令行参数，并保存到tornado.options.optrons
    tornado.options.parse_command_line()
    print("list = ", tornado.options.options.list)
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])
    httpServer = tornado.httpserver.HTTPServer(app)
    # 使用变量的值
    httpServer.bind(tornado.options.options.port)
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()