import tornado.web
from tornado.web import RequestHandler

import os
import config

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        url = self.reverse_url("kaigegood")
        self.write("<a href='%s'>去另一个界面</a>"%(url))

#重定向
class RedirectHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect("/")

class SunckHandler(RequestHandler):
    # 该方法会在HTTP方法之前调用
    def initialize(self, word1, word2):
        self.word1 = word1
        self.word2 = word2
    def get(self, *args, **kwargs):
        self.write("sunck is a nice man")


class KaigeHandler(RequestHandler):
    def initialize(self, word3, word4):
        self.word3 = word3
        self.word4 = word4
    def get(self, *args, **kwargs):
        self.write("kaige is a nice man")



class LiuyifeiHandler(RequestHandler):
    def get(self, p1, p2, p3, *args, **kwargs):
        print(p1 + "-" + p2 + "-" + p3)
        self.write("liuyifei is a nice women")



class ZhangmanyuHandler(RequestHandler):
    def get(self, *args, **kwargs):
        alist = self.get_arguments("a")
        print(alist[0], alist[1])
        self.write("zhangmanyu is a good women")

#post
class PostFileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('postfile.html')
    def post(self, *args, **kwargs):
        name = self.get_argument("username")
        passwd = self.get_body_argument("passwd")
        hobbyList = self.get_body_arguments("hobby")
        print(name, passwd, hobbyList)
        self.write("sunck is a handsome man")

class ZhuyinHandler(RequestHandler):
    def get(self, *args, **kwargs):
        print(self.request.method)
        print(self.request.host)
        print(self.request.uri)
        print(self.request.path)
        print(self.request.query)
        print(self.request.version)
        print(self.request.headers)
        print(self.request.body)
        print(self.request.remote_ip)
        print(self.request.files)
        self.write("zhuyin is a good women")


class UpFileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('upfile.html')
    def post(self, *args, **kwargs):
        filesDict = self.request.files
        for inputname in filesDict:
            fileArr = filesDict[inputname]
            for fileObj in fileArr:
                # 存储路径
                filePath = os.path.join(config.BASE_DIRS, 'upfile/' + fileObj.filename)
                with open(filePath, "wb") as f:
                    f.write(fileObj.body)
        self.write("ok")










#wirte
class WriteHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("sunck is a good man")
        self.write("sunck is a nice man")
        self.write("sunck is a handsome man")
        #刷新缓冲区,关闭当次请求通道
        #在finish下边就不要在write
        self.finish()
        self.write("sunck is a cool man")



#json
import json
class Json1Handler(RequestHandler):
    def get(self, *args, **kwargs):
        per = {
            "name": "sunck",
            "age": 18,
            "height": 175,
            "weight": 70
        }
        #将字典转换成json字符串
        jsonStr = json.dumps(per)
        self.set_header("Content-Type","application/json; charset=UTF-8")
        self.set_header("sunck", "good")
        self.write(jsonStr)
class Json2Handler(RequestHandler):
    def get(self, *args, **kwargs):
        per = {
            "name": "kaige",
            "age": 18,
            "height": 175,
            "weight": 70
        }
        self.write(per)


class HeaderHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "text/html; charset=UTF-8")
        self.set_header("kaige", "nice")
    def get(self, *args, **kwargs):
        self.set_header("kaige", "handsome")
        self.write("good nice")
    def post(self, *args, **kwargs):
        pass


class StatusCodeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("************************")
        self.set_status(999)



#错误处理
class ErrorHandler(RequestHandler):
    def write_error(self, status_code, **kwargs):
        if status_code == 500:
            code = 500
            #返回500界面
            self.write("服务器内部错误")
        elif status_code == 404:
            code = 404
            #返回404界面
            self.write("资源不存在")
        self.set_status(code)
    def get(self, *args, **kwargs):
        flag = self.get_query_argument("flag")
        print(type(flag))
        if flag == '0':
            self.send_error(404)
        self.write("you are right")

