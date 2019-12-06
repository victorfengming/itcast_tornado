import os

BASE_DIR = os.path.dirname(__file__)

# 参数
options = {
    "port": 8080
}

settings = {
    # 这写key的名字可不是随便起的奥,是写好的,
    # 就像upfile就没有,你写了也白扯
    'template_path': os.path.join(BASE_DIR, "templates"),
    'static_path': os.path.join(BASE_DIR, "static"),
    "debug": True
    # "autoreload" : True
}
# 配置
