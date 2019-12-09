#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by victor

# 本模块的功能:<同步异步demo>

# 这个就相等于一个客户端的请求
import time


# 添加一个耗时的操作
def longIO():
    print("开始耗时操作")
    time.sleep(5)
    print("结束耗时操作")


def reqA():
    print("开始处理reqA")
    longIO()
    print("结束处理reqA")


# 这个就相等于另一个客户端的请求
def reqB():
    print("开始处理reqB")
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