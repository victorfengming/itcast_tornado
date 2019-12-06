from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.write("main page info tornado!")


class SunckHandler(RequestHandler):
    # 该方法会在HTTP方法之前调用
    def initialize(self,age,name) -> None:
        self.age = age
        self.name = name

    def get(self):
        print(self.age)
        print(self.name)
        self.write("sunck page info tornado!")

