from typing import Any

from config import BASE_DIR
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def initialize(self) -> None:
        print("init_initialize")

    def prepare(self):
        print("prepare")

    def get(self):
        self.send_error(500)
        print("get_start")
        self.write("main page info tornado!")

    def set_default_headers(self) -> None:
        print(":set_default_headers")

    def write_error(self, status_code: int, **kwargs: Any) -> None:
        print("write_error")
        self.write("服务器内部错误!!!")
    def on_finish(self) -> None:
        print("on_finish")

class WriteHandler(RequestHandler):

    def get(self):
        self.write("write page info tornado!")
        self.write("write page nicie tornado!")
        self.write("write page coll tornado!")
        self.write("write page beautiful tornado!")
        '''
        你会发现他们是连着的,因为我都写在了缓冲区里面
        '''
        # 刷新缓冲区, 并关闭当前请求通道
        self.finish()
        # 如果我不写他,当我们的程序结束,他也会刷新了
        # 下面这行就写丢了
        self.write("write page wonderful tornado!")

    def post(self):
        pass



