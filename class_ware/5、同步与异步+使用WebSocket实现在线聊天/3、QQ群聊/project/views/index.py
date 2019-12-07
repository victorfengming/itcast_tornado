import tornado.web
from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler

class StaticFileHandler(tornado.web.StaticFileHandler):
    def __init__(self, *args, **kwargs):
        super(StaticFileHandler, self).__init__(*args, **kwargs)
        self.xsrf_token

class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('home.html')

class ChatHandler(WebSocketHandler):
    users = []
    def open(self):
        self.users.append(self)
        for user in self.users:
            user.write_message(u"[%s]登陆了"%(self.request.remote_ip))

    def on_message(self, message):
        for user in self.users:
            user.write_message(u"[%s]说:%s"%(self.request.remote_ip, message))

    def on_close(self):
        self.users.remove(self)
        for user in self.users:
            user.write_message(u"[%s]退出了"%(self.request.remote_ip))

    def check_origin(self, origin):
        return True
