# 本章大纲
第10章介绍了什么是异常，如何生成异常，异常处理，Python对异常的支持，如何创建自定义的异常类、断言。


# 知识点
## 10.1 什么是异常
### 10.1.1 错误
当 Python 检测到一个错误时，解释器会指出当前语句已经无法继续执行下去， 这时候就出现了异常。

- **语法错误**：必须在编译前解决。
- **逻辑错误**：运行时出现，如：非法的输入、边界值溢出等。


### 10.1.2 异常
异常是程序出现错误而在正常控制流以外采取的行为。

该行为分为**两个阶段**：

1. **产生异常**：当符合异常的产生条件时，解释器就会触发一个异常。异常可以是Python解释器触发的，也可以是coder手动触发的。
2. **处理异常**：异常引发后，指示程序如何执行，是忽略错误继续执行还是终止程序。


**异常处理的好处**：使得程序具有在运行时管理错误的能力，在错误发生时采取可靠的补救措施。


## 10.2 Python 中的常见异常

- `ZeroDivisionError`：除数为零
- `NameError`：访问没有定义的变量
- `SyntaxError`：唯一不是在运行时发生的异常，语法错误导致程序编译失败。
- `IndexError`：请求的索引超出序列范围
- `KeyError`：请求一个不存在的字典关键字
- `IOError`：输入/输出错误
- `AttributeError`：访问未知的对象属性


## 10.3 检测和处理异常
检测和处理异常有两种主要形式: `try-except` 和 `try-finally`。


### 10.3.1 try-except 语句
```python
try:
    try_suite       # watch for exceptions here
except Exception[, reason]:
    except_suite    # exception-handling code
```

`try-except`的处理流程：

1. 异常被引发后，`try` 语句块中异常发生点后的剩余语句不会被执行；
2. Python 解释器搜索对应的异常处理器，一旦找到就开始执行处理器中的代码；
3. 如果没有找到合适的异常处理器, 那么异常就自底向上移交给调用者去处理（最顶层也无法处理则退出程序）。


### 10.3.2 带有多个 `except` 的 `try` 语句
```python
def safe_float(obj):
    try:
        retval = float(obj)
    except ValueError:
        retval = 'could not convert non-number to float'
    except TypeError:
        retval = 'object type cannot be converted to float'
    return retval
```


### 10.3.3 同时处理多个异常的 `except` 语句
```python
def safe_float(obj):
    try:
        retval = float(obj)
    except (ValueError, TypeError):
        retval = 'argument must be a number or numeric string'
    return retval
```


### 10.3.4 异常的层次结构
```
|- BaseException
  |- KeyboardInterrupt
  |- SystemExit
  |- Exception
     |- (all other current built-in exceptions)
```


### 10.3.5 异常参数
```python
# multiple exceptions
except (Exception1,..., ExceptionN)[, reason]:
    suite_for_Exception1_to_ExceptionN_with_Argument
```


上面的`reason`是一个包含异常代码诊断信息的类**实例**，异常参数自身会组成一个元组并存储为`reason`的属性`args`。

------------

获取异常的错误信息：
```python
def safe_float(object):
  try:
      retval = float(object)
  except (ValueError, TypeError), e:
      retval = str(e)
  return retval
```


### 10.3.6 `else` 子句

`else`子句执行的条件：`try`范围中的所有代码没有引发异常。

```python
try:
    module.function()
except:
    print 'error'
else:
    print 'success'
```


### 10.3.7 `finally` 子句
`finally` 子句：是无论是否有异常发生，都会执行的一段代码。


### 10.3.8 `try-finally` 语句
```python
try:
    A
finally:
    B
```
当在 `try` 范围中产生一个异常时会立即跳转到 `finally` 语句，当 `finally` 语句执行完毕后会继续向上一层引发异常。


### 10.3.9 `try-except-else-finally` 语句
```python
try:
    A
except MyException:
    B
else:
    C
finally:
    D
```

结果：A-C-D[正常] 或 A-B-D[异常]

### 10.3.10 `try`语句后跟子句的总结

- 有`else`子句则一定要有`except`子句
- `finally`子句前可以没有`except`或`else`子句


## 10.4 上下文管理
### 10.4.1 with 语句
`with` 语句用来简化`try-except-finally`语句，仅工作于支持上下文管理协议(context management protocol)的对象。

```python
with open('/etc/passwd', 'r') as f:
    for eachLine in f:
        # ...do stuff with eachLine or f...
```
### 10.4.2 上下文管理协议
上下文管理器必须实现的方法：

- `__context__()`：提供上下文对象
- `__enter__()`：完成 with 语句块执行前的准备工作
- `__exit__()`：当 with 语句块执行结束调用


`contextlib` 模块的 `functions/decorators`，可以方便地创建上下文管理器。


## 10.5 字符串作为异常（过时）
Python 1.5 前，标准的异常是基于字符串实现的，但是从现在起建议使用异常类。


## 10.6 触发异常
通过 `raise` 语句，可手动触发异常。


语法：`raise [SomeException [, args [, traceback]]]`
- `SomeException`：字符串/异常类/实例
- `args`：异常的参数是一个元组
- `traceback`：用于exception—normally的追踪对象


例子：
```python
try:
    raise IOError, 'raise test'
except IOError, e:
    print e
```


## 10.7 断言
`assert`可用于触发异常：如果断言成功不采取任何措施，否则触发`AssertionError`。


语法：`assert expr[, args]`

实例：
```python
try:
    assert 1 == 0, 'One does not equal zero silly!'
except AssertionError, args:
    print '%s: %s' % (args.__class__.__name__, args)
    # AssertionError: One does not equal zero silly!
```


断言的原理：
```python
def assert(expr, args=None):
    if __debug__ and not expr:
        raise AssertionError, args
```


## 10.8 标准异常
所有的标准/内建异常、自定义异常都是继承自根异常 `BaseException` 。
（其他信息见 [10.2 Python中的常见异常](#10.2) 和 [10.3.4 异常的层次结构](#10.3.4)）


## 10.9 使用异常的目的与好处

**目的：** 为了使程序足够健壮，可以处理理应用级别的错误（不至于灾难性地影响其执行环境），并提供用户级别的错误信息。

**好处：** 异常不仅简化代码，而且简化整个错误管理体系。


## 10.10 异常和 sys 模块
通过 `sys` 模块中 `exc_info()` 获取**异常信息**。

```python
import sys


try:
    float('abc123')
except:
    exc_tuple = sys.exc_info()
    print exc_tuple
    """ (<type 'exceptions.ValueError'>,
    ValueError('could not convert string to float: abc123',),
    <traceback object at 0x0000000002AB3848>) """
```


`sys.exc_info()` 得到的元组是：

- `exc_type`：异常类
- `exc_value`：异常类的实例
- `exc_traceback`：追踪对象，提供了发生异常的上下文，包含代码的执行帧、异常发生时的行号等信息。


## 10.11 异常相关的标准库
- `exceptions`：内建异常
- `contextlib`：使用 `with` 语句的上下文对象工具
- `sys`：包含各种异常相关的对象和函数(见 `sys.ex*`)


# 练习
**10–1. 引发异常. 以下的哪个因素会在程序执行时引发异常? 注意这里我们问的并不是异常的原因. **

a) 用户 
b) 解释器 
c) 程序 
**d) 以上所有 **
e) 只有 b) 和 c) 
f) 只有 a) 和 c)


**10–2. 引发异常. 参考上边问题的列表, 哪些因素会在运行交互解释器时引发异常?**

I/O（文件不存在、读取错误）、系统错误、边界值溢出等。


**10–3. 关键字. 用来引发异常的关键字有那些?**

`raise`、`try`


**10–4. 关键字. try-except 和 try-finally 有什么不同?**

- `try-except`：当`try`代码块运行出错，`except`代码块才会被执行（匹配到相应异常时），处理完异常后`try-except`后的代码会继续往下执行；
- `try-finally`：不管`try`代码块是否出现异常，最终都会执行`finally`里的代码。如果出现异常，执行完`finally`代码块后，异常会继续往上层抛。


**10–5. 异常. 下面这些交互解释器下的 Python 代码段分别会引发什么异常(参阅表 10.2 给出的内建异常清单):**

```
(a)  >>> if 3 < 4 then: print '3 IS less than 4!'
(b)  >>> aList = ['Hello', 'World!', 'Anyone', 'Home?']
     >>> print 'the last string in aList is:', aList[len(aList)]
(c)  >>> x
(d)  >>> x = 4 % 0
(e)  >>> import math
     >>> i = math.sqrt(-1)
```
(a) `SyntaxError`
(b) `IndexError`
(c) `NameError`
(d) `ZeroDivisionError`
(e) `ValueError`


**10–6. 改进的 open(). 为内建的 open() 函数创建一个封装. 使得成功打开文件后, 返回文件句柄; 若打开失败则返回给调用者 None , 而不是生成一个异常. 这样你打开文件时就不需要额外的异常处理语句.**

```python
def myopen(path, access='r'):
    try:
        f = open(path, access)
    except (IOError, ValueError):
        return None
    return f


if __name__ == '__main__':
    print myopen("test.txt", 'abc')
```


**10–7. 异常. 下面两段 Python 伪代码 a) 和 b) 有什么区别? 考虑语句 A 和 B 的上下文环境.**

```python
(a)  try:
        statement_A
     except . . .:
        . . .
     else:
        statement_B


(b)  try:
        statement_A
        statement_B
     except . . .:
        . . .
```

**情况1：** 如果`statement_A`执行出错，则(a)和(b)都不会执行`statement_B`；

**情况2：** 如果`statement_A`执行正常，则(a)和(b)都会执行`statement_B`——**但是**，如果`statement_B`的执行也出错，(b)可以在`except`子句里捕获到异常并做处理，而(a)则只能将`statement_B`产生的异常抛给上层调用者。


**10–8. 改进的 raw_input() . 本章的开头, 我们给出了一个"安全"的 float() 函数, 它建立在内建函数 float() 上, 可以检测并处理 float() 可能会引发的两种不同异常. 同样, raw_input() 函数也可能会生成两种异常, EOFError (文件末尾 EOF, 在 Unix 下是由于按下了 Ctrl+D 在 Dos 下是因为 Ctrl+Z) 或 是 KeyboardInterrupt (取消输入 , 一 般是由于按下了Ctrl+C). 请创建一个封装函数 safe_input() , 在发生异常时返回 None .**
```python
def safe_input(msg):
    data = None
    try:
        data = raw_input(msg)
    except (EOFError, KeyboardInterrupt):
        pass
    return data


if __name__ == '__main__':
    print safe_input("please input: ")
```


**10–9. 改进的 math.sqrt(). math 模块包含大量用于处理数值相关运算的函数和常量. 不幸的是, 它不能识别复数, 所以我们创建了 cmath 模块来支持复数相关运算. 请创建一个 safe_sqrt() 函数, 它封装 math.sqrt() 并能处理负值, 返回一个对应的复数.**

```python
import math, cmath


def safe_sqrt(num):
    try:
        result = math.sqrt(num)
    except ValueError:
        result = cmath.sqrt(num)
    return result


if __name__ == '__main__':
    print safe_sqrt(123)
    print safe_sqrt(-123)
```
