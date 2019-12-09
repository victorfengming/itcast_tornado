'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor
'''
# 本模块的功能:<>


# 这个就相等于一个客户端的请求
import time
import threading


def genCoroutine(func):
    '''
    这个好多人就屡不清了
    '''
    def wapper(*args, **kwargs):
        '''
        这样的话这个装饰器就麻烦了,因为我还得要这个全局的gen啊
        我需要获得多个生成器
        '''
        gen1 = func()  # reqA的生成器
        gen2 = next(gen1)  # longIO的生成器

        # 在这里面创建我的线程
        # 挂起他
        def run(g):
            # 这个就是执行longIO去了
            res = next(g)
            try:
                gen1.send(res)  # 返回给reqA数据
            except StopIteration as e:
                # 啥都不干
                pass

        threading.Thread(
            target=run, args=(gen2,)
        ).start()

    return wapper


# 添加一个耗时的操作
# handler获取数据,(数据库,其他服务器,循环耗时)
def longIO():
    '''
    现在你只需要知道你的耗时的操作是啥,
    线程的东西你不用管了
    tornado都帮你弄好了
    '''
    print("开始耗时操作")
    time.sleep(3)
    print("结束耗时操作")
    # 结束耗时操作后的返回数据
    yield "victor is a cool man"


@genCoroutine
def reqA():
    print("开始处理reqA")
    res = yield longIO()
    print("接受到longIO的数据为：", res)
    # 这里就相当于挂起了
    print("结束处理reqA")


# 这个就相等于另一个客户端的请求
def reqB():
    print("开始处理reqB")
    time.sleep(1)
    print("结束处理reqB")


def main():
    reqA()
    reqB()
    while True:
        time.sleep(0.1)


if __name__ == '__main__':
    main()
