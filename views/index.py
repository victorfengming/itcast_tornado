from typing import Any

from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.write("main page info tornado!")
        self.write("<br>")

        url2 = self.reverse_url("postfile")
        self.write("<a href='%s'>去表单页面</a>" % (url2))
        # self.write("<a href="+url+">去另一个页面</a>")



class GoodHandler(RequestHandler):

    def get(self,p1,p3,p2):

        self.write("GoodHandler kaige !")
        self.write("<br>")
        self.write(p3)
        self.write("<br>")
        self.write(p2)
        self.write("<br>")
        self.write(p1)




class DoPostfileHandler(RequestHandler):
    # 这里执行接受post参数的操作
    pass
class PostfileHandler(RequestHandler):

    def get(self):
        self.render("index/postfile.html")
