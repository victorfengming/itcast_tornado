from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.write("main page info tornado!")
class HomeIndexHandler(RequestHandler):
    def get(self):
        temp = 100
        # 直接传一个变量就行
        per = {
            "name":"victor",
            "age":21,
        }
        flag = 0
        stus = [
            "张三",
            "李四",
            "王五",
            "赵柳",
            "田七",
        ]
        self.render("home.html",num = temp,**per,flag = flag,stus = stus)
        # self.render("home.html")
