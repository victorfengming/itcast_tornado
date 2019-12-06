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
    '''
    用于上传文件的视图类,其中包含显示表单的get方法
    和用于处理上传的POST方法
    '''
    # get方法,加载表单模板
    def get(self):
        self.render("upfile.html")

    # 文件上传指定是POST请求啦
    def post(self):
        # 用于接收上传的信息
        self.write("上传成功!")
        # 通过request.files对象来获取所有文件对象内容
        contents = self.request.files
        # 遍历最大的字典,拿到没个name类型的字典的键
        # 其中content是字典中的键,比如file,img
        for content in contents:
            # 通过键获取值,拿到相同name的文件列表
            # 这个filearr,就是一个list
            fileArr = contents[content]
            # 遍历文件列表
            # 这个fileObj又是一个dict字典类型
            for fileObj in fileArr:
                # 定义存储路径
                # 通过BASE_DIR来获取服务器的绝对位置
                # 其中通过这个fileObj的字典的filename键,
                # 来获取文件名字,来定义存储路径的文件名称
                file_path = os.path.join(BASE_DIR,"upfile/"+fileObj.filename)
                # 写入文件
                with open(file_path,"wb") as f:
                    # 文件的内容就是body
                    f.write(fileObj.body)
                    # TODO 这里还需要处理的就是,用户上传同名文件
                    #  导致文件重新在服务器中覆盖的问题
                print("文件写入成功")



