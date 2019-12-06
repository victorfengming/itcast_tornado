from typing import Any

from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.write("main page info tornado!")
        self.write("<br>")
        url = self.reverse_url("kaige")
        self.write("<a href='%s'>去另一个页面</a>" % (url))
        # self.write("<a href="+url+">去另一个页面</a>")


class SunckHandler(RequestHandler):
    # 该方法会在HTTP方法之前调用
    def initialize(self, age, name) -> None:
        self.age = age
        self.name = name

    def get(self):
        print(self.age)
        print(self.name)
        self.write("sunck page info tornado!")


class StatusHandler(RequestHandler):

    def get(self):
        self.set_status(999, "我是谁,我在哪,我要干神马")
        self.write("status page info tornado!")


class RedirectHandler(RequestHandler):

    def get(self):
        # 直接就重定向了
        self.redirect("/")


class ErrorHandler(RequestHandler):

    def write_error(self, status_code: int, **kwargs: Any) -> None:
        if status_code == 500:
            self.write("服务器内部错误500了")
        elif status_code == 404:
            self.write("资源不存在")
        else:
            self.write("我也不知道是啥错误")

    def get(self):
        # 直接就重定向了
        flag = self.get_query_argument("flag")
        if flag == '0':
            print("有错误")
            self.send_error(500)
            # 这里抛出错误,下面就不会执行了

        print("没毛病")

        self.write("you are right!")


class KaigeHandler(RequestHandler):

    def get(self):
        self.write("hansklg kaige !")
