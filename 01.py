import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):
    '''
    主页处理函数
    '''
    
    def get(self):
        '''
        这个get不是随便写的,是框架提前定义好的
        :return:
        '''
        
        
        self.write("main page info tornado!")

if __name__ == '__main__':
    app = tornado.web.Application([(r"/",IndexHandler)])
    

    httpServer = tornado.httpserver.HTTPServer(app)
    
    # httpServer.listen(8000)
    # 这里不用listen了,我们用bind
    # 将服务器绑定到指定的端口上
    httpServer.bind(8000)
    # 这里我写几个就开几个进程
    '''
    默认开启一个进程
    如果大于0,开启多个进程
    值为none或者小于等于0的话,就开启对应硬件机器CPU核心数的子进程
    '''
    httpServer.start(5)
    # 这个bind和start加一起就相当于 httpServer.listen(8000)了
    # 近期你可以多些一点,以为你要对于创建服务器的流程有一个了解,以后随便写


    # app.listen() 只能在单继承模式中使用
    '''
    多进程: 虽然tornado给我们提供了一次性启动多进程的方式,
        但是由于一些原因,我们不建议使用这种方式,来启动多进程,
        而是手动启动多进程,并且还能绑定多个端口
    多进程有三个问题:
        1. 每个紫禁城都会从父进程中复制出一份IOloop的实例,
            如果在创建紫禁城钱,修改了IOloop,会影响到所有的紫禁城实例
        2. 所有的进程都是由一个命令启动的,无法做到在不停止服务的情况下修改代码,这样不好
        3. 所有进程共享一个端口,想要进行监控,有点难
    我自己来启动的话,能在一个进程运行后,修改源代码,来单独在运行一遍,也OK
    '''

    tornado.ioloop.IOLoop.current().start()
