from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.write("main page info tornado!")


class HomeIndexHandler(RequestHandler):
    def get(self):
        def funcSum(a, b):
            return a + b

        self.render("home.html", func=funcSum)


class CartHandler(RequestHandler):
    def get(self):
        self.render("cart.html")


# 数据库
class StudentsHandler(RequestHandler):
    def get(self):
        # 去数据库中提取数据
        stus = [
            {"name": "张三", "age": 21, "sex": "man"},
            {"name": "李四", "age": 23, "sex": "woman"},
            {"name": "赵六", "age": 22, "sex": "woman"},
            {"name": "田七", "age": 17, "sex": "woman"},
            {"name": "王五", "age": 19, "sex": "woman"},
        ]
        self.render("students.html", stus=stus)
