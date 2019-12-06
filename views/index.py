from typing import Any

from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.write("main page info tornado!")







class UpFileHandler(RequestHandler):

    def get(self):
        self.render("upfile.html")
    def post(self):
        # 用于接收上传的信息
        self.write("上传成功!")
        self.write("上传内容是:")
        contents = self.request.files
        print(contents)
        print(contents.values())
        for content in list(contents.values())[0]:
            filename = content["filename"]
            body = content["body"]
            type = content["content_type"]
            self.write("filename:" + str(filename))
            self.write("body:" + str(body))
            self.write("type:"+str(type))
            self.write("-------------------<br>")

