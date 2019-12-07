import tornado.web
from tornado.web import RequestHandler

from models import Students

class IndexHandler(RequestHandler):
    def initialize(self):
        print("initialize")
    def prepare(self):
        print("prepare")
    def get(self, *args, **kwargs):
        print("HTTP方法")
        self.send_error(500)
        self.write("sunck is a good man")
    def set_default_headers(self):
        print("set_default_headers")
    def write_error(self, status_code, **kwargs):
        print("write_error")
        self.write("服务器内部错误……")
    def on_finish(self):
        print("on_finish")


class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        num = 100
        per = {
            "name":"sunck",
            "age": 18
        }
        flag = 0
        stus = [
            {
                "name":"hanmeimei",
                "age":20
            },
            {
                "name":"lilei",
                "age":21
            }
        ]
        self.render('home.html', num = num, **per, flag = flag, stus = stus)



class FuncHandler(RequestHandler):
    def get(self, *args, **kwargs):
        def mySum(n1, n2):
            return n1 + n2
        self.render('market.html', ms = mySum)



class TransHandler(RequestHandler):
    def get(self, *args, **kwargs):
        str = "<h1>sunck is a good man</h1>"
        self.render('trans.html', str = str)


class CartHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('cart.html', title = "cart")



#数据库
class StudentsHandler(RequestHandler):
    def get(self, *args, **kwargs):
        #去数据库中提取数据
        # stu = Students("fghjkiuhbn",567)
        # stu.save()
        # self.write("ok")
        stus = Students.all()
        self.render('students.html', stus = stus)














