import timeit

def test1():
    x=0
    for i in range(1000000):
        if i%5:
            x+=i
    return x

def test2():
    x=0
    for i in xrange(1000000):
        if i%5!=0:
            x+=i
    return x

def test3():
    x=0
    for i in xrange(1000000):
        if not i%5:
            pass
        else:
            x+=i
    return x

def test4():
    x=0
    for i in xrange(1000000):
        if i%5==0:
            pass
        else:
            x+=i
    return x

t1=timeit.Timer("test1()","from __main__ import test1")
print '1',t1.timeit(10)#修改执行次数
t2=timeit.Timer("test2()","from __main__ import test2")
print '2',t2.timeit(10)#修改执行次数
t3=timeit.Timer("test3()","from __main__ import test3")
print '3',t3.timeit(10)#修改执行次数
t4=timeit.Timer("test4()","from __main__ import test4")
print '4',t4.timeit(10)#修改执行次数
