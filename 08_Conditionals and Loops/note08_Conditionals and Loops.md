# 本章大纲
介绍条件和循环语句的用法、迭代器、列表解析和生成器表达式。

# 知识点
## 8.1 if-elif-else
switch-case的替代方案：

- 使用字典替代让代码更优雅。
- 使用if-elif-else替代

使用映射对象(比如字典)的一个最大好处就是它的搜索操作比类似 if-elif-else 语句或是 for 循环这样的序列查询要快很多.

## 8.2 条件表达式

- 表达式：`X if C else Y`
- 旧的写法：`smaller = (x < y and [x] or [y])[0]`
- 新的写法：`smaller = x if x < y else y`

## 8.3 for循环
在列表解析和生成器表达式中, 它会自动地调用迭代器的 `next()` 方法, 捕获 `StopIteration` 异常并结束循环(所有这一切都是在内部发生的).

### 8.3.1 迭代器
迭代器对象有一个 `next()` 方法, 调用后返回下一个条目. 所有条目迭代完后, 迭代器引发一 个 `StopIteration` 异常告诉程序循环结束. for 语句在内部调用` next() `并捕获异常

### 8.3.2 xrange()

- 当范围列表很大时, `xrange()` 比 `range()` 更为适合
- `xrange()`不会在内存里创建列表的完整拷贝. 它只被用在for循环中, 在for循环外使用它没有意义。
- 它的性能远高出`range()`, 因为它不生成整个列表, 而是返回一个可迭代对象(不是列表也不是一个迭代器)

### 8.3.3 与序列相关的内建函数
- `sorted()` 和 `zip()`：返回一个序列
- `reversed()` 和 `enumerate()`：返回迭代器

## 8.4 pass语句
`pass` 语句表示不做任何事情，即 NOP(No OPeration) 。从汇编语言中借用这个概念，可以用来标记未来要完成的代码。

## 8.5 else语句
在 while 和 for 循环中使用 else 语句时, 只要 for 循环是正常结束的(不是通过 break ), else 子句就会执行

## 8.6 迭代器和 iter() 函数

用for循环对字典进行迭代，遍历的是keys
用for循环对文件进行迭代，遍历的是每一行数据。

```python
>>> s = 'abc'
>>> fetch = iter(s)
>>> fetch
<iterator object at 0x0000000002592390>
>>> while True:
...   try:
...     i = fetch.next()
...   except StopIteration:
...     break
...   print i
```
**注意：**
在迭代序列的时候删除元素，会立即反映到所迭代的item上（序号发生变化），所以最好不要这样操作——因为：迭代器是与实际对象绑定在一起的。

## 8.7 列表解析

- `[x**2 for x in range(6)]`
- 过滤出被2整除不为0的元素：`filter(lambda x: x % 2, seq)` 或 `[x for x in seq if x % 2]`
- 3行5列元组：`[(x+1, y+1) for x in range(3) for y in range(5)]`
- 计算一个文本文件总的非空白字符数：`sum([len(word) for line in f for word in line.split()])`
- `map(lambda x:x+x,range(5))`   #lambda 函数，各项+本身
- `reduce(lambda x,y:x+y,range(1,3),5)` #lambda 函数，5是初始值， 5+(1+2)

**列表解析的性能缺陷**：必须生成所有的数据用以创建整个列表，当数据量很大时影响迭代效率。

## 8.8 生成器表达式
**生成器**：和列表解析非常相似，但并不真正创建列表, 而是返回一个生成器，这个生成器在每次计算出一个item后，就把这个item产出（yield）。生成器表达式使用了"延迟计算"(lazy evaluation), 所以它在使用内存上更有效。


e.g.1 计算一个文本文件的非空白字符总数：
`sum(len(word) for line in open('data.txt') for word in line.split())`


e.g.2 计算一个大文本文件的最长行的字符数：
`max(len(line) for line in open('data.txt'))`


e.g.3 交叉配对例子：
```python
rows = [1, 2, 3, 17]
def cols(): # example of simple generator
  yield 56
  yield 2
  yield 1

x_product_pairs = ((i, j) for i in rows for j in cols())
for pair in x_product_pairs:
  print pair
```


# 练习
**8.1 **
(a)CE (b)DE (c)BE

**8.2 **
*略*

**8.3 **
(a) `range(10)`
(b) `range(3, 19, 3)`
(c) `range(-20, 861, 220)`

**8–4. 素数. 我们在本章已经给出了一些代码来确定一个数字的最大约数或者它是否是一个素数. 请把相关代码转换为一个返回值为布尔值的函数，函数名为 isprime() . 如果输入的是一个素数, 那么返回 True , 否则返回 False。**
```python
def isprime(num):
    if num < 2:
        return False
    elif num == 2:
        return True

    n = int(num ** 0.5)
    while n > 1:
        if num % n == 0:
            return False
        else:
            n -= 1
    else:
        return True
```

**8–5. 约数. 完成一个名为 getfactors() 的函数. 它接受一个整数作为参数, 返回它所有约数的列表, 包括 1 和它本身。**
```python
def getfactors(num):
    if num <= 0:
        return []

    result = set([])
    n = int(num ** 0.5)
    while n > 0:
        tmp = divmod(num, n)
        if tmp[1] == 0:
            result.add(n)
            result.add(tmp[0])
        n -= 1

    return sorted([x for x in result])
```

**8–6. 素因子分解. 以刚才练习中的 isprime() 和 getfactors() 函数为基础编写一个函 数, 它接受一个整数作为参数, 返回该整数所有素数因子的列表. 这个过程叫做求素因子分解, 它输出的所有因子之积应该是原来的数字. 注意列表里可能有重复的元素. 例如输入 20 , 返回结果应该是 [2, 2, 5] .**
```python
def prime_split(num):
    if num <= 1:
        return []
    if isprime(num):
        return [num]

    factors = getfactors(num)
    if len(factors) > 2:
        result = []
        maxF = factors[-2]
        tmp = divmod(num, maxF)
        result += prime_split(maxF)
        result += prime_split(tmp[0])
        return sorted(result)
    else:
        return []
```

**8–7. 全数. 完全数被定义为这样的数字: 它的约数(不包括它自己)之和为它本身. 例如: 6 的约数是 1, 2, 3, 因为 1 + 2 + 3 = 6 , 所以 6 被认为是一个完全数. 编写一个名为 isperfect()的函数, 它接受一个整数作为参数, 如果这个数字是完全数, 返回 1 ; 否则返回 0 .**
```python
def isperfect(num):
    factors = prime_split(num)
    factors.insert(0, 1)
    return sum(factors) == num
```

**8–8. 阶乘. 一个数的阶乘被定义为从 1 到该数字所有数字的乘积. N 的阶乘简写为 N! . 写一个函数, 指定 N, 返回 N! 的值.**
```python
def factorial(N): # N! = 1*2*3...*N
    if N <= 0:
        return None
    return reduce(lambda x,y:x*y, range(1,N+1))
```

**8–9. Fibonacci 数列. Fibonacci 数列形如 1, 1, 2, 3, 5, 8, 13, 21, 等等. 也就是说, 下一个值是序列中前两个值之和. 写一个函数, 给定 N , 返回第 N 个 Fibonacci 数字. 例如, 第 1 个 Fibonacci 数字是 1 , 第 6 个是 8 .**
```python
def Fibonacci(N):
    if N <= 2:
        return 1
    tmp = [1,1]
    for x in range(2,N):
        tmp.append(tmp[-2]+tmp[-1])
    return tmp[-1]
```

**8–10. 文本处理. 统计一句话中的元音, 辅音以及单词(以空格分割)的个数. 忽略元音和辅音的特殊情况, 如 "h", "y", "qu" 等. 附加题: 编写处理这些特殊情况的代码.**

*略。*

**8–11. 文本处理. 要求输入一个姓名列表，输入格式是“Last Name, First Name,” 即 姓, 逗号, 名. 编写程序处理输入, 如果用户输入错误, 比如“ First Name Last Name,” , 请纠正这 些错误, 并通知用户. 同时你还需要记录输入错误次数. 当用户输入结束后, 给列表排序, 然后以 "姓 , 名" 的顺序显示.**
```python
num = int(raw_input('Enter total number of names: '))
i = 0
error_count = 0
names = []
while i < num:
    name = raw_input('Please enter name %d: ' % i)
    if ', ' not in name:
        print '>> Wrong format... should be Last, First.'
        error_count += 1
        print '>> You have done this %d time(s) already. Fixing input. . .' % error_count
        nameTmp = name.split()
        name = nameTmp[0] + ', ' + nameTmp[1]
    names.append(name)
    i += 1
else:
    print 'The sorted list (by last name) is:'
    names.sort()
    for name in names:
        print '\t%s' % name
```

**8-12**

*略。*

**8–13. 程序执行性能. 在 8.5.2 节里, 我们介绍了两种基本的迭代序列方法:**
**(1) 通过序列项 (2) 通过序列索引遍历. 该小节的末尾我们指出后一种方法在序列很长的时候性能不佳. (在我的系统下, 性能差了将近两倍[83%]) 你认为它的原因是什么?**

后者通过序列索引遍历时，在序列很长的时候`len()`方法计算序列的大小时会比较耗时，导致性能不佳。
