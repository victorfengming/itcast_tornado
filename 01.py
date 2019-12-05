import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

"""
通常如果程序非正常结束
就会出现:"通常每个套接字地址(协议/网络地址/端口)只允许使用一次"
这是因为端口没有没释放
这时我们的debug模式还没开启

tornado为我们提供了一tornado.option模块
用于全局参数的定义/存储/转换
option:
    不让端口写死,让option这个值从外部传进来
基础方法与属性:
help : 其实就是选项变量的帮助提示信息,一般不用         
"""

# 这个函数的原型
'''
def define(
    name: str,
    default: Any = None,
    type: type = None,
    help: str = None,
    metavar: str = None,
    multiple: bool = False,
    group: str = None,
    callback: Callable[[Any], None] = None,
) -> None:
'''
# 这个函数的功能
'''
用来定义option选项变量的方法
'''
# 参数
'''
name : 选项变量名,必须保证其唯一性,否则会爆出一个option already define 错误
default : 设置选项变量的默认值,如果不传,默认为none
type : 设置选项变量的类型,比如int,从命令行或者配置文件导入参数时,
    tornado会根据输入的数据类型的值进行转换
    会根据类型转换成对应的值,转换不成,会报错,那么就有问题了
    可以:int float str datetime timedelta
    如果没有设置type,会根据default的值进行转换,
    如果default没有设置,他就不进行转换
multiple : 设置选项变量是否可以为多个值,默认为false    
'''

# 好我们可以先写一个
tornado.options.define("port", default=8000, type=int)
# 我们要接受一个列表,列表里面的元素的字符串类型,默认给个空
tornado.options.define("list", default=[], type=str,multiple=True)

# 然后我们还有一个属性
'''
tornado.options.options
全局的options对象
所有定义的选项变量都会作为改对象的属性
'''

# 获取参数的方法
'''
我们不是把这些参数赋值了么,我们还要把这些参数存储起来
tornado.options.parse_command_line()
    作用:
        转换命令行参数,将命令行参数抓换成为option的属性
'''


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("main page info tornado!")


if __name__ == '__main__':
    # 转换命令行参数,并保存在tornado.options.options里面
    tornado.options.parse_command_line()
    # 可以打印一下list
    print('list->',tornado.options.options.list)
    app = tornado.web.Application([(r"/", IndexHandler)])

    httpServer = tornado.httpserver.HTTPServer(app)
    # 使用变量的值
    httpServer.bind(tornado.options.options.port)

    httpServer.start(1)

    tornado.ioloop.IOLoop.current().start()

    # 这样我们在启动的时候就能不需要修改代码就能指定端口号了
    # 代码能少改就少改变
    '''
    (venv) D:\PycharmProjects\itcast_tornado>python 01.py --port=9000 --list=good,nice,handsome,cool
    list-> ['good', 'nice', 'handsome', 'cool']
    [I 191205 17:13:54 web:2246] 200 GET / (127.0.0.1) 1.00ms
    [W 191205 17:13:54 web:2246] 404 GET /favicon.ico (127.0.0.1) 1.00ms
    '''