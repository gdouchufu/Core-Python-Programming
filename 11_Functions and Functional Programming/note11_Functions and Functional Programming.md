# 本章大纲
介绍函数的创建、调用方式，内部函数、函数装饰器、函数参数的定义和传递、函数式编程、变量作用域、闭包。

# 知识点

## 11.1 什么是函数？

- 函数是对程序逻辑进行结构化或过程化的一种编程方法，以实现代码的复用。
- python 的过程就是函数，因为解释器会隐式地返回默认值 `None`。
- python 动态地确定函数返回类型，而不是进行直接的类型关联。
- 可以使用 `type()` 函数作为代理，处理有不同参数类型的函数的多重声明，以模拟其他编程语言的函数重载。

## 11.2 调用函数

### 11.2.1 关键字参数
解释器能通过给出的关键字来匹配参数的值。

### 11.2.2 参数组
`func(*tuple_grp_nonkw_args, **dict_grp_kw_args)`：`tuple_grp_nonkw_args` 是以元组形式体现的非keyword参数组, `dict_grp_kw_args` 是装有keyword参数的字典。

### 11.3 创建函数
先声明 `foo()`，再声明` bar()`，接着调用 `foo()`（foo()里调用bar()），而`bar()`已经存在了所以调用成功。

### 11.3.1 函数属性
```python
def bar():
    pass

bar.__doc__ = 'Oops, forgot the doc str above'
bar.version = 0.1

print bar.__doc__
print bar.version
```

### 11.3.2 内部/内嵌函数
**内部函数：** python 支持静态地嵌套域，可以在函数体内创建另外一个函数。

创建方式：
```python
def foo():
    def bar():
        print 'bar() called'

    print 'foo() called'
    bar()

foo()
```

### 11.3.3 函数装饰器
- 装饰器是在函数调用之上的修饰，当仅当声明一个函数的时候，才会被额外调用。
- 装饰器类似于Java的注解，是AOP（Aspect Oriented Programming，面向切面编程）的思想。

```python
@deco1(deco_arg)
@deco2
def func(): pass
```
= `func = deco1(deco_arg)(deco2(func))`


**用途：**

- 引入日志
- 增加计时逻辑来检测性能
- 给函数加入事务的能力

## 11.4 传递函数
```python
def bar(argfunc):
    argfunc()

bar(foo)
```

## 11.5 形式参数
### 11.5.1 位置参数
位置参数必须以在被调用函数中定义的准确顺序来传递。

### 11.5.2.默认参数
所有的位置参数必须出现在任何一个默认参数之前。

```python
>>> def taxMe(cost, rate=0.0825):
...     return cost + (cost * rate)
>>> taxMe(100)
108.25
>>> taxMe(100, 0.05)
105.0
```


## 11.6 可变长度的参数
在函数调用中使用`*`和`**`符号，允许函数接收在函数声明中定义的形参之外的参数。

### 11.6.1.非关键字可变长参数（元组）
```python
def tupleVarArgs(arg1, arg2='defaultB', *theRest):
    'display regular args and non-keyword variable args'
    print 'formal arg 1:', arg1
    print 'formal arg 2:', arg1
    for eachXtrArg in theRest:
        print 'another arg:', eachXtrArg

>>> tupleVarArgs('abc', 123, 'xyz', 456.789)
formal arg 1: abc
formal arg 2: 123
another arg: xyz
another arg: 456.789
```

### 11.6.2.关键字变量参数（Dictionary）
关键字变量参数必须为函数定义的最后一个参数：`def function_name([formal_args,][*vargst,] **vargsd)`

```python
def newfoo(arg1, arg2, *nkw, **kw):
    'display regular args and all variable args'
    print 'arg1 is:', arg1
    print 'arg2 is:', arg2
    for eachNKW in nkw:
        print 'additional non-keyword arg:', eachNKW
    for eachKW in kw.keys():
        print "additional keyword arg '%s': %s" % \
            (eachKW, kw[eachKW])

newfoo('wolf', 3, 'projects', freud=90, gamble=96)
'''
arg1 is: wolf
arg2 is: 3
additional non-keyword arg: projects
additional keyword arg 'gamble': 96
additional keyword arg 'freud': 90
'''
```

### 11.6.3 调用带有可变长参数对象函数
```python
aTuple = (6, 7, 8)
aDict = {'z': 9}
newfoo(1, 2, 3, x=4, y=5, *aTuple, **aDict)
'''
arg1 is: 1
arg2 is: 2
additional non-keyword arg: 3
additional non-keyword arg: 6
additional non-keyword arg: 7
additional non-keyword arg: 8
additional keyword arg 'y': 5
additional keyword arg 'x': 4
additional keyword arg 'z': 9
'''
```

## 11.7 函数式编程
### 11.7.1 匿名函数与 lambda
- 用 lambda 关键字创造匿名函数。
- **lambda 表达式的目的在于优化性能，在调用时绕过函数的栈分配。**

```python
a = lambda x, y=2 : x+y

>>> a(3)
5
>>> a(3,4)
7
```
### 11.7.2 内建函数 apply()、filter()、map()、reduce()

#### 11.7.2.1 apply()
`apply()`在1.6版本以前用来支持函数的可变参数，已过时。

#### 11.7.2.2 filter()
`filter(bool_func, seq)`： `bool_func`为序列`seq`的每个元素调用所给定的布尔函数，将每次 filter 返回的非零（true)值元素添加到返回列表中。

```python
def odd(n):
    return n % 2
filter(odd, allNums)
```
= `filter(lambda n : n % 2, allNums)`
= `[n for n in allNums if n%2]`
=
```python
>>> from random import randint as ri
>>> print [n for n in [ri(1,99) for i in range(9)] if n%2]
[39, 7, 51, 83]
```

#### 11.7.2.3 map()
`map()` 将函数调用“映射”到每个序列的元素上，并返回一个含有所有返回值的列表。

**`map()` 与单个序列：**
```python
>>> map((lambda x: x+2), [0, 1, 2, 3, 4, 5])
[2, 3, 4, 5, 6, 7]
>>> map(lambda x: x**2, range(6))
[0, 1, 4, 9, 16, 25]
>>>[x**2 for x in range(6)]
[0, 1, 4, 9, 16, 25]
```

**`map()` 与多个序列：**
```python
>>> map(lambda x, y: x + y, [1,3,5], [2,4,6])
[3, 7, 11]
>>>
>>> map(lambda x, y: (x+y, x-y), [1,3,5], [2,4,6])
[(3, -1), (7, -1), (11, -1)]
>>>
>>> map(None, [1,3,5], [2,4,6])
[(1, 2), (3, 4), (5, 6)]
>>>
>>> zip([1,3,5], [2,4,6])
[(1, 2), (3, 4), (5, 6)]
```

#### 11.7.2.4 reduce()
`reduce()`通过取出序列的头两个元素，将他们传入二元函数来获得一个单一的值来实现。

`reduce(func, [1, 2, 3])` <=> `func(func(1, 2), 3)`

```python
>>> reduce((lambda x,y: x+y), range(5))
10
```

### 11.7.3 偏函数应用
- Currying概念将函数式编程的概念和默认参数以及可变参数结合在一起。一个带 n 个参数， curried 的函数固化第一个参数为固定参数， 并返回另一个带 n-1 个参数函数对象。
- Currying 能泛化成为偏函数应用（PFA：Partial Function Application）， 这种函数将任意数量（顺序）的参数的函数转化成另一个带剩余参数的函数对象。
- PFA 是在 python2.5 的时候被引入的，通过 functools 模块能很好的给用户调用。

```python
>>> from operator import add, mul
>>> from functools import partial
>>> add1 = partial(add, 1)     # add1(x) == add(1, x)
>>> mul100 = partial(mul, 100) # mul100(x) == mul(100, x)
>>>
>>> add1(10)
11
>>> mul100(10)
1000
```

**将二进制字符串转换成为整数：** `baseTwo(x) == int(x, base=2)`
```python
>>> baseTwo = partial(int, base=2)
>>> baseTwo.__doc__ = 'Convert base 2 string to an int.'
>>> baseTwo('10010')
18
```

## 11.8 变量作用域
### 11.8.1 全局变量与局部变量
- 当搜索一个变量名的时候，Python解释器先从局部作用域开始搜索；
- 如果在局部作用域内没有找到改变量名，就会在全局域搜索这个变量名；
- 如果在全局域也找不到则抛出 `NameError` 异常。

### 11.8.2 global 语句
`global` 将局部变量变为全局变量。
```python
>>> is_this_global = 'xyz'
>>> def foo():
...     global is_this_global
...     this_is_local = 'abc'
...     is_this_global = 'def'
...     print this_is_local + is_this_global
...
>>> foo()
abcdef
>>> print is_this_global
def
```


### 11.8.3 闭包
- 如果在一个内部函数里，对在外部作用域(但不是在全局作用域）的变量存在进行引用，那么内部函数就被认为是 closure。
- 定义在外部函数内的但由内部函数引用或者使用的变量被称为自由变量，使用函数的 func_closure 属性来追踪自由变量。
- closurs 多用于 GUI 或者在很多 API 支持回调函数的事件驱动编程中。回调是函数，闭包也是函数，但是他们能携带一些额外的作用域。
- 对自由变量的引用是存储在cell对象里（cell是在作用域结束后使自由变量的引用存活的一种基础方法）

```python
def counter(start_at=0):
     count = [start_at]
     def incr():
         count[0] += 1
         return count[0]
     return incr
count = counter(5)
print count()
print count()

count2 = counter(100)
print count2()
print count()

''' result:
6
7
101
8
'''
```

### 11.8.4 作用域和 lambda
```python
x = 10
def foo():
    y = 5
    bar = lambda z:x+z
    print bar(y) # 15
    y = 8
    print bar(y) # 18
foo()
```

## 11.9 递归
```python
def factorial(n):
    if n == 0 or n == 1: # 0! = 1! = 1
        return 1
   else:
        return (n * factorial(n-1))
```

## 11.10 生成器
- 挂起返回出中间值并多次继续的协同程序被称为生成器。
- 当等待一个生成器的时候，生成器能立刻返回控制。
- 在调用的生成器能挂起（返回一个结果）之前，调用生成器返回一个结果而不是阻塞等待那个结果返回。
- 那就是 yield 语句返回一个值给调用者并暂停执行。当生成器的 next()方法被调用的时候，它会准确地从离开地方继续。

### 11.10.1 简单的生成器
```python
from random import randint
def randGen(aList):
    while len(aList) > 0:
         yield aList.pop(randint(0, len(aList)))

for item in randGen(['rock', 'paper', 'scissors']):
    print item

'''
scissors
rock
paper
'''
```

### 11.10.2 加强的生成器特性
在 python2.5 中，一些加强特性加入到生成器中，除了 `next()`来获得下个生成的值，还可以将值回送`send()`给生成器，以及要求生成器退出`close()`。

```python
def counter(start_at=0):
    count = start_at
    while True:
        val = (yield count)
        if val is not None:
            count = val
        else:
            count += 1

>>> count = counter(5)
>>> count.next()
5
>>> count.next()
6
>>> count.send(9)
9
>>> count.next()
10
>>> count.close()
>>> count.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

# 练习
**11–1.参数。比较下面 3 个函数：**

*略。*

**11-2.函数。结合你对练习 5-2 的解，以便你创建一个带相同对数字并同时返回一它们之和以及产物的结合函数。**

*略。*

**11-3 函数。在这个练习中，我们将实现 max()和 min()内建函数。**

(a) 写一个带两个元素的 max2() 和 min2()函数，分别返回一个较大和较小元素。举例来说，max2(4,8)和 min2(4,8)会各自每次返回 8 和 4。

(b) 创建使用了在 a 部分中的解来重构 max()和 min()的新函数 my_max()和 my_min().这些函数分别返回非空队列中一个最大和最小值。它们也能带一个参数集合作为输入。用数字和字符串来测试你的解。

```python
def max2(num1, num2):
    return num1 if num1 >= num2 else num2

def my_max(seq):
    return reduce(max2, seq)

print my_max([1,5,2,7,3])
```

**11–4. 返回值。给你在 5-13 的解创建一个补充函数。创建一个带以分为单位的总时间以及返回一个以小时和分为单位的等价的总时间。**

*略。*

**11–5. 默认参数。更新你在练习 5-7 中创建的销售税脚本以便让销售税率不再是函数输入的必要之物。 创建使用你地方税率的默认参数如果在调用的时候没有值传入。**

*略。*

**11–6. 变长参数。下一个称为 printf()的函数。有一个值参数，格式字符串。剩下的就是根据格式化字符串上的值，要显示在标准输出上的可变参数，格式化字符串中的值允许特别的字符串格式操作指示符，如%d, %f, etc。提示：解是很琐碎的—-无需实现字符串操作符功能性，但你需要显示用字符串格式化操作（%）**

*略。*

**11-7. 用map()进行函数式编程。给定一对同一大小的列表，如[1,2,3]和[‘abc’,’def,‘ghi’, …，将两个标归并为一个由每个列表元素组成的元组的单一的表，以使我们的结果看起来像这样：{[（1,‘abc’）, （2,‘def’）, （3,‘ghi’）, …]。（虽然这问题在本质上和第6章的一个问题相似，那时两个解没有直接的联系）然后创建用zip内建函数创建另一个解。**

```python
print map(None, [1,2,3], ['abc','def','ghi'])
print zip([1,2,3], ['abc','def','ghi'])
```

**11–8. 用 filer()进行函数式编程.使用练习 5-4 你给出的代码来决定闰年。更新你的代码一 边他成为一个函数如果你还没有那么做的话。然后写一段代码来给出一个年份的列表并返回一个只 有闰年的列表。然后将它转化为用列表解析。**

```python
years = [1900,2000,2004]
print filter(lambda year:(year%4==0 and year%100!=0) or (year%400==0),years)
print [year for year in years if (year%4==0 and year%100!=0) or (year%400==0)]
```

**11–9. 用 reduce()进行函数式编程。复习 11.7.2 部分，阐述如何用 reduce()数字集合的累加的代码。修改它，创建一个叫 average()的函数来计算每个数字集合的简单的平均值。**

```python
def average(arr):
    return reduce((lambda x,y : x+y), arr) / float(len(arr))

print average([1,23,4,3])
```

**11–10.用 filter()进行函数式编程。在 unix 文件系统中，在每个文件夹或者目录中都有两个 特别的文件：'.'表示现在的目录，'..'表示父目录。给出上面的知识，看下 os.listdir()函数的文档并描述这段代码做了什么：`files = filter(lambda x: x and x[0] != '.', os. listdir(folder))`**

列出folder目录下所有非隐藏文件（文件名以`.`开头）

**11–11.用 map()进行函数式编程。写一个使用文件名以及通过除去每行中所有排头和最尾的空白来“清洁“文件。在原始文件中读取然后写入一个新的文件，创建一个新的或者覆盖掉已存在的。 给你的用户一个选择来决定执行哪一个。将你的解转换成使用列表解析。**

`lines = filter(lambda line : line.strip()+'\n', open('test.txt'))`

**11–12. 传递函数。给在这章中描述的 testit()函数写一个姊妹函数。timeit()会带一个函数对象（和参数一起）以及计算出用了多少时间来执行这个函数，而不是测试执行时的错误。返回下面的状态：函数返回值，消耗的时间。你可以用 time.clock()或者 time.time()，无论哪一个给你提供了较高的精度。 （一般的共识是在 POSIX 上用 time.time()， 在 win32 系统上用 time.clock()） 注意：timeit()函数与 timeit 模块不相关(在 python2.3 中引入）**

```python
import time

def timeit(func, *nkwargs, **kwargs):
    begin = time.clock()
    try:
        retval = func(*nkwargs, **kwargs)
        result = (True, retval, time.clock()-begin)
    except Exception, diag:
        result = (False, str(diag))
    return result

def test():
    funcs = (int, long, float)
    vals = (1234, 12.34, '1234', '12.34')

    for eachFunc in funcs:
        print '-' * 20
        for eachVal in vals:
            retval = timeit(eachFunc, eachVal)
            if retval[0]:
                print '%s(%s) =' % \
                      (eachFunc.__name__, `eachVal`), retval[1]
                print 'cost time(s): %s' % `retval[2]`
            else:
                print '%s(%s) = FAILED:' % \
                      (eachFunc.__name__, `eachVal`), retval[1]

if __name__ == '__main__':
    test()
```

**11–13.使用 reduce()进行函数式编程以及递归。在第 8 章中，我们看到 N 的阶乘或者 N!作为 从 1 到 N 所有数字的乘积。**

(a)用一分钟写一个带 x,y 并返回他们乘积的名为 mult(x,y)的简单小巧的函数。
`def mult(x, y): return x * y`

(b)用你在 a 中创建的 mult()函数以及 reduce 来计算阶乘。
`reduce(mult, range(1, 4+1))`

(c)彻底抛弃掉 mult()的使用，用 lamda 表达式替代。
`reduce(lambda x, y : x * y, range(1, 4+1))`

(d)在这章中，我们描绘了一个递归解决方案来找到 N!用你在上面问题中完成的 timeit()函数， 并给三个版本阶乘函数计时(迭代的，reduce()以及递归）

```python
import time

def iterator_N(N):
    result = 1
    for n in range(1, N+1):
        result *= n
    return result

def reduce_N(N):
    return reduce(lambda x, y : x * y, range(1, N+1))

def recursive_N(N):
    if N == 0 or N == 1:
        return 1
    else:
        return N * recursive_N(N-1)

def timeit(func, *nkwargs, **kwargs):
    begin = time.clock()
    try:
        retval = func(*nkwargs, **kwargs)
        result = (True, retval, time.clock()-begin)
    except Exception, diag:
        result = (False, str(diag))
    return result

if __name__ == '__main__':
    funcs = (iterator_N, reduce_N, recursive_N)
    N = 4
    for func in funcs:
        retval = timeit(func, N)
        if retval[0]:
            print '%s(%s) =' % \
                  (func.__name__, `N`), retval[1]
            print 'cost time(s): %s' % `retval[2]`
        else:
            print '%s(%s) = FAILED:' % \
                  (func.__name__, `N`), retval[1]
```

**11–15.递归。从写练习 6-5 的解，用递归向后打印一个字符串。用递归向前以及向后打印一个字符串。**
```python
def backward(s,i=0):
    if i < len(s):
        print s[0:i+1],
        backward(s,i+1)

def forward(s,j=0):
    if j > -len(s):
        print s[j-1:],
        forward(s,j-1)

if __name__=='__main__':
    backward('abcdefg')
    print
    forward('abcdefg')
```

**11–16. 更新 easyMath.py。这个脚本，如例子 11.1 描绘的那样，以入门程序来帮助年轻人强化他们的数学技能。通过加入乘法作为可支持的操作来更进一步提升这个程序。额外的加分：也加入除法；这比较难做些因为你要找到有效的整数除数。幸运的是，已经有代码来确定分子比分母大， 所以不需要支持分数。**

```python
from operator import add, sub, mul, div
from random import randint, choice

ops = {'+': add, '-': sub, '*': mul, '/':div}
MAXTRIES = 2

def doprob():
    op = choice('+-*/')
    nums = [randint(1, 10) for i in range(2)]
    nums.sort(reverse=True)

    if (op == '/'):
        while nums[0] % nums[1] != 0:
            nums = [randint(1, 10) for i in range(2)]
            nums.sort(reverse=True)

    ans = ops[op](*nums)
    pr = '%d %s %d = ' % (nums[0], op, nums[1])
    oops = 0
    while True:
        try:
            if int(raw_input(pr)) == ans:
                print 'correct'
                break
            if oops == MAXTRIES:
                print 'answer\n%s%d' % (pr, ans)
            else:
                print 'incorrect... try again'
                oops += 1
        except (KeyboardInterrupt, \
                EOFError, ValueError):
            print 'invalid input... try again'


def main():
    while True:
        doprob()
        try:
            opt = raw_input('Again? [y]').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break


if __name__ == '__main__':
    main()
```

**11–17.定义**
**(a) 描述偏函数应用和 currying 之间的区别。**

偏函数解决这样的问题：如果我们有函数是多个参数的，我们希望能固定其中某几个参数的值。

Currying解决的是一个完全不同的问题：如果我们有几个单参数函数，并且这是一种支持一等函数(first-class)的语言，如何去实现一个多参数函数？函数加里化是一种实现多参数函数的方法。

**(b) 偏函数应用和闭包之间有什么区别？**

闭包：一个可以使用另外一个函数作用域中的变量的函数。

偏函数：偏应用函数就是缺少部分或全部参数的函数

**(c) 最后，迭代器和生成器是怎么区别开的？**

生成器是迭代器的真子集。

**11–18. 同步化函数调用。复习下第6章中当引入浅拷贝和深拷贝的时候，提到的丈夫和妻子情形（6\. 20小结）。他们共用了一个普通账户，同时对他们银行账户访问时会发生不利影响。创建一个程序，让调用改变账户收支的函数必需同步。换句话说，在任意给定时刻只能有个一进程或者线程来执行函数。一开始你试着用文件，但是一个真正的解决方法是用装饰器和在threading或者mutex模块中的同步指令。你看看第17章来获得更多的灵感。**

*略。*
