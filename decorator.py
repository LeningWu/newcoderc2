# !-*-coding:utf-8 -*-
# !/usr/bin/env/python
# !@Time     :2018/10/10  16:42
# !@Author   :Lening Wu
# !@File    decorator.py

def log(level, *args, **kvargs):
    def inner(func):
        '''
        * 无名字参数
        ** 有名字参数
        '''

        def wrapper(*args, **kvargs):
            print (level, 'before calling ', func.__name__)
            print (level, 'args', args, 'kvargs', kvargs)
            func(*args, **kvargs)
            print (level, 'end calling ', func.__name__)

        return wrapper
    return inner


@log(level='INFO')
def hello(name, age):
    print ('hello', name, age)

if __name__ == '__main__':
    hello(name='nowcoder', age=2) #= log(hello())
