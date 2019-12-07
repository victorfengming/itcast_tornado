import tornado.web
from tornado.web import RequestHandler
from tornado.httpclient import AsyncHTTPClient

import json
import time

class StaticFileHandler(tornado.web.StaticFileHandler):
    def __init__(self, *args, **kwargs):
        super(StaticFileHandler, self).__init__(*args, **kwargs)
        self.xsrf_token

class Students1Handler(RequestHandler):
    def on_response(self, response):
        if response.error:
            self.send_error(500)
        else:
            data = json.loads(response.body)
            self.write(data)
        self.finish()

    @tornado.web.asynchronous #不关闭通信的通道
    def get(self, *args, **kwargs):
        #获取所有学生的信息
        # time.sleep(30)
        url = "http://s.budejie.com/topic/tag-topic/64/hot/budejie-android-6.6.9/0-20.json?market=xiaomi&ver=6.6.9&visiting=&os=7.1.1&appname=baisibudejie&client=android&udid=863254032906009&mac=02%3A00%3A00%3A00%3A00%3A00"
        #创建客户端
        client = AsyncHTTPClient()
        client.fetch(url, self.on_response)

class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("home")




class Students2Handler(RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        url = "http://s.budejie.com/topic/tag-topic/64/hot/budejie-android-6.6.9/0-20.json?market=xiaomi&ver=6.6.9&visiting=&os=7.1.1&appname=baisibudejie&client=android&udid=863254032906009&mac=02%3A00%3A00%3A00%3A00%3A00"
        client = AsyncHTTPClient()
        res = yield client.fetch(url)
        if res.error:
            self.send_error(500)
        else:
            data = json.loads(res.body)
            self.write(data)




class Students3Handler(RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        res = yield self.getData()
        self.write(res)

    @tornado.gen.coroutine
    def getData(self):
        url = "http://s.budejie.com/topic/tag-topic/64/hot/budejie-android-6.6.9/0-20.json?market=xiaomi&ver=6.6.9&visiting=&os=7.1.1&appname=baisibudejie&client=android&udid=863254032906009&mac=02%3A00%3A00%3A00%3A00%3A00"
        client = AsyncHTTPClient()
        res = yield client.fetch(url)
        if res.error:
            ret = {"ret":0}
        else:
            ret = json.loads(res.body)
        raise tornado.gen.Return(ret)