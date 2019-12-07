import os
BASE_DIRS = os.path.dirname(__file__)

#参数
options = {
    "port": 8000
}

#数据库配置
mysql = {
    "host": "10.0.144.21",
    "user": "root",
    "passwd": "sunck",
    "dbName": "test"
}

#配置
settings = {
    "static_path": os.path.join(BASE_DIRS, "static"),
    "template_path": os.path.join(BASE_DIRS, "templates"),
    "debug": True,
    "cookie_secret":"t63VyFj+T4uz+OwspKnQv50hXM9+skLTh1s1Tbaqa5Q=",
    "xsrf_cookies": True,
    "login_url":"/login"
}

