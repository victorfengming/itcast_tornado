import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

# 获取参数的方法
# 好我们可以先写一个
tornado.options.define("port", default=8000, type=int)
# 我们要接受一个列表,列表里面的元素的字符串类型,默认给个空
tornado.options.define("list", default=[], type=str, multiple=True)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("main page info tornado!")


if __name__ == '__main__':
    tornado.options.parse_config_file("config")
    # 可以打印一下list
    print('list->', tornado.options.options.list)
    app = tornado.web.Application([(r"/", IndexHandler)])

    httpServer = tornado.httpserver.HTTPServer(app)
    # 使用变量的值
    httpServer.bind(tornado.options.options.port)

    httpServer.start(1)

    tornado.ioloop.IOLoop.current().start()
