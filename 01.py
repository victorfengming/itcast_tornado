import tornado.web
'''
tornado的基础web框架模块
'''
import tornado.ioloop
'''
tornado的核心IO循环模块,
封装了Linux的epoll和BSD的kqueue
这个是tornado高效的基础
'''

# 引入httpserver模块
import tornado.httpserver

# 业务处理类
# 类比Django的视图
class IndexHandler(tornado.web.RequestHandler):
    '''
    主页处理函数
    '''

    # 处理GET请求的
    def get(self):
        '''
        这个get不是随便写的,是框架提前定义好的
        :return:
        '''
        # 对应HTTP请求的方法
        # 给浏览器响应信息
        self.write("main page info tornado!")


if __name__ == '__main__':
    # 这个路由和django差不多,只不过这个调用的是一个类
    # 实例化app应用对象
    # Application是tornado框架的核心,与服务器对接的接口
    # 里面保存了路由映射表,有一个listen方法,用来创建一个HTTP服务器的实例,并绑定了端口
    app = tornado.web.Application([(r"/",IndexHandler)])

    # 这个只是绑定在8000端口,注意:并没有进行监听奥
    # app.listen(8000)
    # 实例化一个http服务器对象
    httpServer = tornado.httpserver.HTTPServer(app)
    # 绑定端口
    httpServer.listen(8000)
    # 这个和上面的listen可不一样,两个对象的方法,不同
    # 说白了,上面的一行,相当于我们这个两行代码的和
    # 这也就是tornado不用像Django那样加上runserver参数启动服务器了
    # 以为代码中写了

    tornado.ioloop.IOLoop.current().start()

