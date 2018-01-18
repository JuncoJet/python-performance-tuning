import timeit
from hashlib import md5, sha1
from zlib import crc32

def test1():
    global z
    for i in range(1000000):
        x=md5()
        x.update(z)
        x=x.hexdigest()
    return x

def test2():
    global z
    for i in range(1000000):
        x=sha1()
        x.update(z)
        x=x.hexdigest()
    return x

def test3():
    global z
    for i in range(1000000):
        x=hex(crc32(z))[2:]
    return x

def test4():
    global z
    for i in range(1000000):
        x=hex(hash(z))[2:]
    return x

z="AA"*32
t1=timeit.Timer("test1()","from __main__ import test1")
print '1',
x=md5()
x.update(z)
print x.hexdigest(),t1.timeit(10)#修改执行次数
t2=timeit.Timer("test2()","from __main__ import test2")
print '2',
x=sha1()
x.update(z)
print x.hexdigest(),t2.timeit(10)#修改执行次数
t3=timeit.Timer("test3()","from __main__ import test3")
print '3',hex(crc32(z))[2:],t3.timeit(10)#修改执行次数
t4=timeit.Timer("test4()","from __main__ import test4")
print '4',hex(hash(z))[2:],t3.timeit(10)#修改执行次数
