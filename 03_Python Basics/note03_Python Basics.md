# 本章大纲
介绍基本的语法、编码风格、内存管理机制，以一个读写文件的Python程序拉开Python编程的序幕。

# 知识点
## 3.1 语句和语法
- Python 使用缩进来分隔代码组，代码的层次关系通过同样深度的空格或制表符缩进体现。同一代码组的代码行必须严格左对齐（左边有同样多的空格或同样多的制表符）。
- Python 的赋值语句不会返回值。

## 3.2 变量赋值
- 同时给多个变量赋值（类似元组`）：go_surf, get_a_tan_while, boat_size, toll_money = (1,'windsurfing', 40.0, -2.00)`
- 交换两个值：`x, y = y, x`

## 3.3 标识符和关键字
- `__xxx__`：系统定义的名字（`__doc__` | `__class__` | `__name__` | ...）
- `__xxx`：类中的私有变量名

## 3.4 基本风格指南
- 在 Python 解释器输入 `import this` 然后回车可以查看“Pythonic”【以 Python 的方式去编写代码、组织逻辑，及对象行为】
- **尽量使用局部变量代替全局变量**，好处：易维护、提高性能、节省内存。（*在查找全局变量之前，总是先查找本地变量！*）

## 3.5 内存管理
- Python是一种解释型语言，对象的类型和内存占用都是运行时确定的，在赋值时解释器会根据语法和右侧的操作数来决定新对象的类型。
- Python 内部记录着所有使用中的对象各有多少引用，一个内部跟踪变量称为一个**引用计数器**。每个对象各有多少个引用，简称**引用计数**。当对象被创建时， 就创建了一个引用计数， 当这个对象不再需要时（这个对象的引用计数变为0时），它被垃圾回收。
- Python 的垃圾收集器实际上是一个**引用计数器**和一个**循环垃圾收集器**。 当一个对象的引用计数变为 0，解释器会释放掉这个对象和仅有这个对象可访问（可到达）的其它对象。作为引用计数的补充， 垃圾收集器也会留心被分配的总量很大（及未通过引用计数销毁的那些）的对象。 在这种情况下， 解释器会暂停下来，试图清理所有未引用的循环。
- **`del obj`**：删除对象的最后一个引用， 也就是该对象的引用计数会减为0，使该对象就成为垃圾回收机制的回收对象。（注意：任何追踪或调试程序会给一个对象增加一个额外的引用， 这会推迟该对象被回收的时间。）

## 3.6 第一个 Python 程序
简洁的写法：`fobj.writelines(['%s %s' % (x, ls) for x in all])`

## 3.7 常用模块
- PyUnit（测试模块）：`unittest`。
- Debugger（调试模块）: `pdb`，支持断点，代码逐行执行，检查堆栈。它还支持事后调试
- Logger（日志模块）: `logging`，定义了一些函数和类帮助你的程序实现灵活的日志系统。
- Profilers（性能测试模块）: `profile`, `hotshot`, `cProfile`


# 练习

**3–1. 标识符。为什么 Python 中不需要变量名和变量类型声明？**

变量名的作用是指向一个对象，单纯只创建对象而没有变量指向它是允许的；

Python是动态语言，在运行时根据语法和右侧的操作数来决定对象的类型，所以不需要申明变量类型。

**【补充】**

**动态语言和静态语言：**

- *动态、静态是指变量的绑定方式，静态语言在编译时绑定，动态语言可以在运行时随意绑定。*
- Java是静态语言，一个变量定义好了数据类型就不能再改变。如：定义了 `String str = 'hello'` 后，`str = 123` 就不行；
- Python是动态语言，在运行时根据语法和右侧的操作数来决定对象的类型。如：`str = 'hello'`，重新赋值 `str = 123` 是可以的。

**强类型和弱类型：**

- 强类型、弱类型是指变量的类型在运算上下文中是否可以自动转换。
- 对于 `1 + "1000"` 这样一条语句：
 - Python会报错，因为它是强类型语言，不能将"1000"自动转换成1000，再和1相加；
 - 而Perl便能进行自动类型转换，所以它是弱类型。


**3–2. 标识符。为什么 Python 中不需要声明函数类型？**

跟python是动态语言有关，在运行时根据返回类型决定函数类型，如果函数没有显式地`return`一个函数类型的话，那么函数类型是`NoneType`


**3–3. 标识符。为什么应当避免在变量名的开始和和结尾使用双下划线？**

因为类似`__xxx__`的变量名是系统定义的名字，容易发生冲突。

**3–4. 语句。在 Python 中一行可以书写多个语句吗？**

可以，用分号 `;`

**3–5. 语句。在 Python 中可以将一个语句分成多行书写吗？**

可以，用反斜杠 `\`

**3–6. 变量赋值**

**(a)赋值语句 x, y, z = 1, 2, 3 会在 x、y、z 中分别赋什么值？**

`x=1, y=2, z=3`

**(b)执行 z, x, y = y, z, x 后，x、y、z 中分别含有什么值？**

`x=3, y=1, z=2`

**3–7. 标识符。下面哪些是 Python 合法的标识符？如果不是，请说明理由！在合法的标识符中，哪些是关键字？**

1. `int32` (合法标识符)
2. `40XL` (非法标识符 - 以数字开头)
3. `$aving$` (非法标识符 - 以$开头)
4. `printf` (合法标识符)
5. `print` (关键字)
6. `_print` (合法标识符)
7. `this` (关键字)
8. `self` (关键字)
9. `__name__` (合法标识符)
10. `0x40L` (非法标识符 - 以数字开头)
11. `bool` (合法标识符)
12. `true` (合法标识符)
13. `big-daddy` (合法标识符)
14. `2hot2touch` (非法标识符 - 以数字开头)
15. `type` (关键字)
16. `thisIsn'tAVar` (非法标识符 - 含有')
17. `thisIsAVar` (合法标识符)
18. `R_U_Ready` (合法标识符)
19. `Int` (合法标识符)
20. `True` (关键字)
21. `if` (关键字)
22. `do` (关键字)
23. `counter-1` (合法标识符)
24. `access` (合法标识符)
25. `_` (合法标识符)

**3–8. Python 代码。将脚本拷贝到您的文件系统中，然后修改它。可以添加注释，修改提示符（‘>’太单调了）等等，修改这些代码，使它看上去更舒服。**

*略。*

**3–9. 移植。 如果你在不同类型的计算机系统中分别安装有 Python， 检查一下，os.linesep 的值是否有不同。 记下操作系统的类型以及 linesep 的值。**

Linux_x64操作系统：`'\n'`

Windows_x64操作系统：`'\r\n'`

**3–10. 异常。使用类似 readTextFile.py 中异常处理的方法取代makeTextFile.py 中 对 os.path.exists() 的 调 用 。 反 过 来 ， 用 os.path.exists() 取 代readTextFile.py 中的异常处理方法。**

makeTextFile.py：
```python
#!/usr/bin/env python
'makeTextFile.py -- create text file'
  
import os
ls = os.linesep
  
# get filename
fname = raw_input('Enter filename: ')
print
  
# get file content (text) lines
all = []
print "\nEnter lines ('.' by itself to quit).\n"
  
# loop until user terminates input
while True:
    entry = raw_input('$ ')
    if entry == '.':
        break
    else:
        all.append(entry)
  
# write lines to file with proper line-ending
try:
    fobj = open(fname, 'w')
except IOError, e:
    print "*** file open error:", e
else:
    fobj.writelines(['%s%s' % (x, ls) for x in all])
    fobj.close()
```

readTextFile.py：
```python
#!/usr/bin/env python
import os
'readTextFile.py -- read and display text file'
 
# get filename
fname = raw_input('Enter filename: ')
print
 
# attempt to open file for reading
if not os.path.exists(fname):
    print "ERROR: '%s' not exists" % fname
else:
    fobj = open(fname, 'r')
    # display contents to the screen
    for eachLine in fobj:
        print eachLine,
    fobj.close()
```

**3–11.字符串格式化 不再抑制 readTextFile.py 中 print 语句生成的 NEWLINE 字符， 修改你的代码， 在显示一行之前删除每行末尾的空白。 这样， 你就可以移除 print 语句末尾的逗号了。**

`eachLine.strip()`

**3–12. 合并源文件。将两段程序合并成一个，给它起一个你喜欢的名字，比方readNwriteTextFiles.py。让用户自己选择是创建还是显示一个文本文件。**
```python
#!/usr/bin/env python
 
import os
ls = os.linesep
 
def readFile():
    # get filename
    fname = raw_input('Enter filename: ')
    print
 
    # attempt to open file for reading
    try:
        fobj = open(fname, 'r')
    except IOError, e:
        print "*** file open error:", e
    else:
        # display contents to the screen
        for eachLine in fobj:
            print eachLine,
        fobj.close()
 
def writeFile():
    # get filename
    while True:
        fname = raw_input('Enter filename: ')
        print
 
        if os.path.exists(fname):
           print "ERROR: '%s' already exists" % fname
        else:
           break
 
    # get file content (text) lines
    all = []
    print "\nEnter lines ('.' by itself to quit).\n"
 
    # loop until user terminates input
    while True:
        entry = raw_input('$ ')
        if entry == '.':
            break
        else:
            all.append(entry)
 
    # write lines to file with proper line-ending
    fobj = open(fname, 'w')
    fobj.writelines(['%s%s' % (x, ls) for x in all])
    fobj.close()
 
while True:
    choose = raw_input('choose action: r | w :')
    if (choose == 'r'):
        readFile()
        break
    elif (choose == 'w'):
        writeFile()
        break
```

**3–13. 添加新功能。 将你上一个问题改造好的 readNwriteTextFiles.py 增加一个新功能：允许用户编辑一个已经存在的文本文件。 你可以使用任何方式，无论是一次编辑一行，还是一次编辑所有文本。需要提醒一下的是， 一次编辑全部文本有一定难度， 你可能需要借助 GUI工具包或一个基于屏幕文本编辑的模块比如 curses 模块。要允许用户保存他的修改（保存到文件）或取消他的修改（不改变原始文件），并且要确保原始文件的安全性（不论程序是否正****常关闭）。**
```python
#!/usr/bin/env python
import os
 
print "************ Text File Editor ************"
print
 
line_sum = 0;
all_content = []
 
# get filename
while True:
    try:
        fname = raw_input('>>> enter filename: ')
        fobj = open(fname, 'r')
        break
    except IOError, e:
        print '>>> [ERROR] file open failed:', e
 
# get original content
for line in fobj.readlines():   
    all_content.append(line)
    print line,
    line_sum += 1
 
def get_new_content():
    while True:
        choose_line_num = raw_input('>>> select one line to edit [1-%d] : ' % line_sum)
        try:
            choose_line_num = int(choose_line_num)
            if not (0 < choose_line_num <= line_sum):
                print '>>> [ERROR] the line number must in [1-%d] !' % line_sum
                continue
            break
        except ValueError, e:
            print '>>> [ERROR] number transform failed: ', e
 
    print '>>> your choose line is : %d' % choose_line_num
    new_content = raw_input('>>> input new content: ')
    all_content[choose_line_num-1] = new_content + os.linesep
 
# generate new content
if line_sum > 0:
    get_new_content()
else:
    print '>>> the file is empty, please input new content directly:'
    new_content = raw_input('>>> ')
    all_content.append(new_content)
 
# save new content
fobj = open(fname, 'w')
for line in all_content:
    fobj.write(line)
fobj.close()
print '>>> save success, bye!'
```

