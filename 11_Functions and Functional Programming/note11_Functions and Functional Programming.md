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

11–9. 用 reduce()进行函数式编程。复习 11.7.2 部分，阐述如何用 reduce()数字集合的累加的代码。修改它，创建一个叫 average()的函数来计算每个数字集合的简单的平均值。

```python
def average(arr):
    return reduce((lambda x,y : x+y), arr) / float(len(arr))

print average([1,23,4,3])
```

**11–10.用 filter()进行函数式编程。在 unix 文件系统中，在每个文件夹或者目录中都有两个 特别的文件：'.'表示现在的目录，'..'表示父目录。给出上面的知识，看下 os.listdir()函数的文档并描述这段代码做了什么：`files = filter(lambda x: x and x[0] != '.', os. listdir(folder))`**

列出folder目录下所有非隐藏文件（文件名以`.`开头）

**11–11.用 map()进行函数式编程。写一个使用文件名以及通过除去每行中所有排头和最尾的空白来“清洁“文件。在原始文件中读取然后写入一个新的文件，创建一个新的或者覆盖掉已存在的。 给你的用户一个选择来决定执行哪一个。将你的解转换成使用列表解析。**

