# Python装饰器 #
  对刚接触Python时间不长的小伙伴来说可能没用过装饰器，甚至也没听说过装饰器。
  在GitHub阅读别人的代码的时候经常看到如下的Python语法
  ```python
def xxx():
    pass
    
@xxx
def func1():
    pass
  ```
  对，这就是装饰器。
## 一个简单的需求 ##
  明明(对!就是那个可以靠脸吃饭的明明)写了一个Python脚本，但是在测试的时候发现脚本执行效率不高，这时候他想到可以在每个函数的开始和结束打印下时间，
  这样就可以看到时间都消耗的哪儿了，然后再对这个函数做优化就可以了。
  Good idea，明明是这么做的
  ```Python
import time
def func_name():
    start_time = time.time()
    #Python sentence
    pass
    print time.time() - start_time
  
  ```
  幸好明明的Python脚本不是很复杂，只定义了十几个函数，虽然花了点时间，但是问题也解决了。问题解决后明明并没有满足于这种解决问题方式。他想，首先这种方式一点都不优雅，每次都在函数中添加那几行代码，之后再删除；
  其次，如果Python中的函数很多几十个甚至上百个的话，再这样做就太低效了。有什么更好的解决之道吗，明明陷入了沉思。
  
  好，带着这个问题让我们一起来学习Python装饰器。
  
## 什么是装饰器 ##
  简单的说，装饰器就是一个能够改变其他函数原有功能的函数，它让Python代码更加的简洁和Pythonic。
  
  

## 参考 ##
1. [python tips](http://book.pythontips.com/en/latest/decorators.html)
2. [how can I make chain of function decorators in python](http://stackoverflow.com/questions/739654/how-can-i-make-a-chain-of-function-decorators-in-python)
3. [廖雪峰Python教程-装饰器](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819879946007bbf6ad052463ab18034f0254bf355000)
4. [知乎-如何理解装饰器](https://www.zhihu.com/question/26930016)
5. [Python装饰器与面向切面编程](http://www.cnblogs.com/huxi/archive/2011/03/01/1967600.html)
6. Fluent Python-Chapter7