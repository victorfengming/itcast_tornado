import os

BASE_DIR = os.path.dirname(__file__)

# 参数
options = {
    "port": 8080
}

mysql = {
    "host":"127.0.0.1",
    "user":"root",
    "passwd":"",
    "dbName":"mydb",

}

settings = {
    # 这写key的名字可不是随便起的奥,是写好的,
    # 就像upfile就没有,你写了也白扯
    'template_path': os.path.join(BASE_DIR, "templates"),
    'static_path': os.path.join(BASE_DIR, "static"),
    "debug": True,
    # "autoreload" : True
    # 这个据说一百亿年才能,用完
    "cookie_secret":"j94bbx0zSY6yYkCgawwJ1bzyM4jzDUuKtLyPC/MMmZA=",
    # 开启保护
    "xsrf_cookies":True,
    "login_url":"/login",
}

# 配置
