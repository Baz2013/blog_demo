# -*- coding:utf-8 -*-

registry = []

#
# def register(func):
#     print('running register(%s)' % func)
#     registry.append(func)
#     return func
#
#
# @register
# def f1():
#     print('running f1()')
#
#
# @register
# def f2():
#     print('running f2()')
#
#
# def f3():
#     print('running f3()')
#
#
# def main():
#     print('running main()')
#     print('registry ->', registry)
#     print f1
#     print f2
#     f1()
#     f2()
#     f3()
import multiprocessing
import time
import sys

class MyProcess(multiprocessing.Process):
    def __init__(self, arg):
        # super(MyProcess, self).__init__()
        multiprocessing.Process.__init__(self)
        self.arg = arg
    def run(self):
        print 'nMask', self.arg
        time.sleep(1)
        sys.exit(0)

if __name__ == '__main__':
    for i in range(10):
        p = MyProcess(i)
        p.start()
    for i in range(10):
    	p.join()

    sys.exit(0)


