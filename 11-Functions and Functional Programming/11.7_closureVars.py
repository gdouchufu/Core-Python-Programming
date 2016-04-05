#!/usr/bin/env python
# coding=utf-8

output = '<int %r id=%#0x value=%d>'
w = x = y = z = 1

def f1():
    # 局部变量，不是全局变量
    x = y = z = 2

    def f2():
	y = z = 3

	def f3():
	    z = 4
	    print output % ('w', id(w), w)
	    print output % ('x', id(x), x)
	    print output % ('y', id(y), y)
	    print output % ('z', id(z), z)

	clo = f3.func_closure
	if clo:
	    print "f3 closure vars:", [str(c) for c in clo]
	else:
	    print "no f3 closure vars"
	f3()

    clo = f2.func_closure
    if clo:
	    print "f2 closure vars:", [str(c) for c in clo]
    else:
	    print "no f2 closure vars"
    f2()

# 定义在外部函数内的但由内部函数引用或者使用的变量被称为自由变量，使用函数的 func_closure 属性来追踪自由变量。
# 如果 f2()使用了任何的定义在 f1()作用域的变量， 比如说， 非全局的和非 f2()的局部域的， 那么它们便是自由变量， 将会被 f1.func_closure 追踪到。
clo = f1.func_closure
if clo:
    print "f1 closure vars:", [str(c) for c in clo]
else:
    print "no f1 closure vars"
f1()

'''
假设函数 f3()已经被传入到其他一些函数，这样便可在稍后，甚至是 f2()完成 之后，调用它。
你不想要让 f2()的栈出现，因为即使我们仅仅在乎 f3()使用的自由变量，栈也会让 所有的 f2()'s 的变量保持存活。
单元维持住自由变量以便 f2()的剩余部分能被释放掉。
'''

'''
在 f3(), f2(), 或者 f1()中都是找不到变量 w 的，所以，这是个全局变量。
在 f3()或者 f2()中，找不到变量 x，所以来自 f1()的闭包变量。
相似地，y 是一个来自 f2() 的闭包变量。最后，z 是 f3()的局部变量。
'''

'''
no f1 closure vars
f2 closure vars: ['<cell at 0x0000000003446558: int object at 0x0000000002A16530>']
f3 closure vars: ['<cell at 0x0000000003446558: int object at 0x0000000002A16530>', '<cell at 0x0000000003446798: int object at 0x0000000002A16518>']
<int 'w' id=0x2a16548 value=1>
<int 'x' id=0x2a16530 value=2>
<int 'y' id=0x2a16518 value=3>
<int 'z' id=0x2a16500 value=4>
'''