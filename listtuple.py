import timeit

def test1():
    x=0
    for i in range(1000000):
        if 'doc' in ['xls','xlsx','pdf','docx','doc','txt']:
            x+=i
    return x

def test2():
    x=0
    for i in xrange(1000000):
        if 'doc' in ('xls','xlsx','pdf','docx','doc','txt'):
            x+=i
    return x

t1=timeit.Timer("test1()","from __main__ import test1")
print '1',t1.timeit(20)#修改执行次数
t2=timeit.Timer("test2()","from __main__ import test2")
print '2',t2.timeit(20)#修改执行次数
