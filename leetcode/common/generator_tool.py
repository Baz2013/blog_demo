# -*- coding:utf-8 -*-

def benchmark(func):
    """
    A decorator that prints the time a function takes
    to execute.
    一个输出函数运行时间的装饰器
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print func.__name__, time.clock() - t
        return res

    return wrapper


def logging(func):
    """
    A decorator that logs the activity of the script.
    一个输出日志信息的装饰器
    (it actually just prints it, but it could be logging!)
    虽然这里只是简单得只用了print函数，但是你可以用其他日志模块代替
    """

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print func.__name__, args, kwargs
        return res

    return wrapper


def counter(func):
    """
    A decorator that counts and prints the number of times a function has been executed
    一个记录、打印函数调用次数的装饰器
    """

    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print "{0} has been used: {1}x".format(func.__name__, wrapper.count)
        return res

    wrapper.count = 0
    return wrapper
