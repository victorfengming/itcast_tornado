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





class PostfileHandler(RequestHandler):

    def get(self):
        self.render("index/postfile.html")


    # 这个地方就比Django厉害了,一个url就能收不同的请求
    def post(self):
        # 接受参数,刚才那个不是叫做get_query么,看这回的
        username = self.get_body_argument("username")
        password = self.get_body_argument("password")
        hobby = self.get_body_arguments("hobby")
        self.write("哈哈,post成了!")
        self.write(username+"--------")
        self.write(password+"--------")
        for i in hobby:
            self.write(i+"--------")
