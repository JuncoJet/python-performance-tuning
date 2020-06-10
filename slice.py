import timeit

def test1():
    i=range(10000)
    x=i[::-1][:10]
    return x

def test2():
    i=range(10000)
    x=i[-1:-10:-1]
    return x

def test3():
    i=range(10000)
    x=i[-10:][::-1]
    return x

for i in range(10):
    t1=timeit.Timer("test1()","from __main__ import test1")
    print '1',t1.timeit(10000)#修改执行次数
    t2=timeit.Timer("test2()","from __main__ import test2")
    print '2',t2.timeit(10000)#修改执行次数
    t3=timeit.Timer("test3()","from __main__ import test3")
    print '3',t3.timeit(10000)#修改执行次数
