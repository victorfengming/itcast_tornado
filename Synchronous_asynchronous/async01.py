'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor
'''
# 本模块的功能:<>


# 这个就相等于一个客户端的请求
import time
import threading

# 添加一个耗时的操作
def longIO(callback):
    def run(cb):
        print("开始耗时操作")
        time.sleep(3)
        print("结束耗时操作")
        cb("victor is a wonderful man")
    threading.Thread(
        target=run,
        args=(callback,)
    ).start()
# 这个longio这部分 ,就像ajax一样都不用我们来写了
'''
这样就会有一个问题,这个run()函数的返回值我们接受不到
为了解决这个问题,我们需要写一个函数,这个函数叫做回调函数
'''
def finish(data):
    print("开始处理回调函数")
    print("接受到longIO的数据为：",data)
    print("结束处理回调函数")

def reqA():
    print("开始处理reqA")
    longIO(finish)
    print("结束处理reqA")


# 这个就相等于另一个客户端的请求
def reqB():
    print("开始处理reqB")
    time.sleep(1)
    print("结束处理reqB")

def main():
    # 这就是同步在处理
    reqA()
    reqB()
    while True:
        '''
        # 如果你要想写死循环,你不要直接写死循环,你得睡一睡
        # 为什么要睡一睡呢,因为你要是不睡你会发现你的CPU利用率占100%
        '''
        time.sleep(0.1)

if __name__ == '__main__':
    main()















'''

       ┌─┐       ┌─┐ + +
    ┌──┘ ┴───────┘ ┴──┐++
    │                 │
    │       ───       │++ + + +
    ███████───███████ │+
    │                 │+
    │       ─┴─       │
    │                 │
    └───┐         ┌───┘
        │         │
        │         │   + +
        │         │
        │         └──────────────┐
        │                        │
        │                        ├─┐
        │                        ┌─┘
        │                        │
        └─┐  ┐  ┌───────┬──┐  ┌──┘  + + + +
          │ ─┤ ─┤       │ ─┤ ─┤
          └──┴──┘       └──┴──┘  + + + +
                 神兽保佑
                代码无BUG!


'''
