import timeit

def test1():
    global z
    for i in range(10000):
        x=("123"*i==z)
    return x

def test2():
    global z,hz
    for i in range(10000):
        x=(hash("123"*i)==hz)
    return x

for i in  [i*8 for i in range(1,10)]:
    z=chr(i+3)*i
    hz=hash(z)
    t1=timeit.Timer("test1()","from __main__ import test1")
    print '1',t1.timeit(100)#修改执行次数
    t2=timeit.Timer("test2()","from __main__ import test2")
    print '2',t2.timeit(100)#修改执行次数
