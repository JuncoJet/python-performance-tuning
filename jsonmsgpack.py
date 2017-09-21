import timeit,json
import msgpack

def test1():
    global dic,data1
    data1=json.dumps(dic)
    return data1

def test2():
    global dic,data2
    data2=msgpack.packb(dic)
    return data2

def test3():
    global data1
    return json.loads(data1)

def test4():
    global data2
    return msgpack.unpackb(data2)

times=1000*1000
data1,data2=None,None
dic={'id':1,'data':{'title':'h1','content':'abcdefg'*100,'list':[1,2,'3'*33,'4']}}
t1=timeit.Timer("test1()","from __main__ import test1")
print '1',t1.timeit(times)
t2=timeit.Timer("test2()","from __main__ import test2")
print '2',t2.timeit(times)
t3=timeit.Timer("test3()","from __main__ import test3")
print '3',t3.timeit(times)
t4=timeit.Timer("test4()","from __main__ import test4")
print '4',t4.timeit(times)
