import timeit
from hashlib import md5, sha1
from zlib import crc32
from ctypes import *

def test1():
    global z
    for i in range(10000):
        x=md5()
        x.update(z)
        x=x.hexdigest()
    return x

def test2():
    global z
    for i in range(10000):
        x=sha1()
        x.update(z)
        x=x.hexdigest()
    return x

def test3():
    global z
    for i in range(10000):
        x=hex(crc32(z))[2:]
    return x

def test4():
    global z
    for i in range(10000):
        x=hex(hash(z))[2:]
    return x

def time33(s):
    h = c_uint(5381);
    for i in range(len(s)):
        h.value=h.value*33+ord(s[i])
    return h.value

l=CDLL("FastHashLib.dll")
def test5():
    global z,l,lz
    for i in range(10000):
        #x=hex(time33(z))
        x=hex(l.time33(z,lz))
    return x

for i in  [i*4 for i in range(1,10)]:
    z=chr(i+3)*i
    lz=len(z)
    t1=timeit.Timer("test1()","from __main__ import test1")
    print '1',
    x=md5()
    x.update(z)
    print x.hexdigest(),t1.timeit(1000)#修改执行次数
    t2=timeit.Timer("test2()","from __main__ import test2")
    print '2',
    x=sha1()
    x.update(z)
    print x.hexdigest(),t2.timeit(1000)#修改执行次数
    t3=timeit.Timer("test3()","from __main__ import test3")
    print '3',hex(crc32(z))[2:],t3.timeit(1000)#修改执行次数
    t4=timeit.Timer("test4()","from __main__ import test4")
    print '4',hex(hash(z))[2:],t4.timeit(1000)#修改执行次数
    t5=timeit.Timer("test5()","from __main__ import test5")
    print '5',hex(c_ulong(l.time33(z,len(z))).value)[2:10],t5.timeit(1000)#修改执行次数
