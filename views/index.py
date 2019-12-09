import tornado.web
from tornado.web import RequestHandler
# 异步的HTTP请求客户端
from tornado.httpclient import AsyncHTTPClient
import json
import time

class StaticFileHandler(tornado.web.StaticFileHandler):
    def __init__(self, *args, **kwargs):
        super(StaticFileHandler, self).__init__(*args, **kwargs)
        self.xsrf_token


class Students1Handler(RequestHandler):
    def on_response(self,response):
        print("刚进到on_response里面n")
        if response.error:
            self.send_error(500)
        else:
            print("开始获取data")
            data = json.loads(response.body)
            print("data获取成功")
            self.write(data)
            print("data写入成功")
        self.finish()

    @tornado.gen.coroutine
    def get(self):
        # 获取所有学生的信息
        # time.sleep(30)
        # 创建客户端
        url = "http://127.0.0.1:8080/home"
        print("url是",url)
        client = AsyncHTTPClient()
        print("客户端创建成功")
        client.fetch(url, self.on_response)

        self.write("students info content!")

class HomeHandler(RequestHandler):
    def get(self):
        # 获取所有学生的信息
        self.write("homo page info!")