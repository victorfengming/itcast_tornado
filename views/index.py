import os
from typing import Any
from config import BASE_DIR
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.write("main page info tornado!")


'''
{
    'file': [
        {'filename': 'a.txt',
         'body': b'suck is a wonderful man',
          'content_type': 'text/plain'
        },

        {'filename': 'reg.md',
          'body': b'x9xa0',
           'content_type': 'application/octet-stream'
        }
    ]
}
'''

class UpFileHandler(RequestHandler):

    def get(self):
        self.render("upfile.html")
    def post(self):
        # 用于接收上传的信息
        self.write("上传成功!")
        self.write("上传内容是:")
        contents = self.request.files
        for content in contents:
            fileArr = contents[content]
            for fileObj in fileArr:
                # 存储路径
                file_path = os.path.join(BASE_DIR,"upfile/"+fileObj.filename)
                with open(file_path,"wb") as f:
                    f.write(fileObj.body)
                print("文件写入成功")



