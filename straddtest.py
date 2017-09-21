import timeit

def test1():
    global str1,times
    x=''
    for i in xrange(times):
        x+=str1+str1
    return x

def test5():
    global str1,times
    x=''
    for i in xrange(times):
        x+=str1*2
    return x

def test4():
    global str1,times
    x=''
    for i in xrange(times):
        x=x+str1
    return x

def test10():
    global str1,times
    x=''
    for i in xrange(times):
        x+=str1
    return x

def test2():
    global str1,times
    x=''
    for i in xrange(times):
        x="%s%s"%(x,str1)
    return x

def test6():
    global str1,times
    x=''
    for i in xrange(times):
        x="%s%s%s"%(x,str1,str1)
    return x

def test3():
    global str1,times
    x=''
    for i in xrange(times):
        x=''.join([x,str1])
    return x

def test7():
    global str1,times
    x=''
    for i in xrange(times):
        x=''.join([x,str1,str1])
    return x

def test8():
    global str1,times
    x=''
    for i in xrange(times):
        x=''.join([x,str1*2])
    return x

def test9():
    global str1,times
    x=''
    for i in xrange(times):
        x=''.join([x,str1+str1])
    return x

times=10000#修改累加次数
str1="abcd"*100#修改字符串长度
t1=timeit.Timer("test1()","from __main__ import test1")
t2=timeit.Timer("test2()","from __main__ import test2")
t3=timeit.Timer("test3()","from __main__ import test3")
t4=timeit.Timer("test4()","from __main__ import test4")
t5=timeit.Timer("test5()","from __main__ import test5")
t6=timeit.Timer("test6()","from __main__ import test6")
t7=timeit.Timer("test7()","from __main__ import test7")
t8=timeit.Timer("test8()","from __main__ import test8")
t9=timeit.Timer("test9()","from __main__ import test9")
t10=timeit.Timer("test10()","from __main__ import test10")
print '1',t1.timeit(1)#修改执行次数
print '2',t2.timeit(1)
print '3',t3.timeit(1)
print '4',t4.timeit(1)
print '5',t5.timeit(1)
print '6',t6.timeit(1)
print '7',t7.timeit(1)
print '8',t8.timeit(1)
print '9',t9.timeit(1)
print '10',t9.timeit(1)

