# 本章大纲
第一章主要讲了Python的起源、特点、Python的安装和运行、Python的实现版本

# 知识点
## 1.1 Python的起源
python创始人 贵铎·范·罗萨姆（Guido van Rossum）为了让程序员更方便容易地写代码，于 1989 年底创造了 Python。
【小故事：蒙提·派森:Monty Python,也称“蒙地蟒蛇”。是英国的一个六人喜剧团体，其七十年代的电视剧和八十年代的电影作品红极一时。贵铎·范·罗萨姆就是该团体的忠实影剧迷，故而将本语言命名为 Python。这里的 IDLE 指的是其成员艾瑞克·艾多 （Eric Idle ）】

## 1.2 Python的特点
- 高级：类json格式的dict和list使得定义数据结构非常方便
- 面向对象
- 可升级：模块化架构，导入模块即可加入新功能，和java类似
- 可扩展
- 可移植：python可以运行在任何带有ANSI C编译器的平台上
- 简洁易读：这是很大的亮点，能用几句代码搞定的事就绝不多写几行
- 解释性和编译性：python是解释型语言，即python程序可以不编译就能够运行。由于不是以本地机器码运行，纯粹的解释型语言通常比编译型语言运行的慢。实际上，Python和Java一样，也是可以字节编译的，其结果就是可以生成一种近似机器语言的中间形式。这不仅改善了 Python 的性能，还同时使它保持了解释型语言的优点。类比PHP，PHP是解释型语言，不能字节编译；类比Java，Java编译型语言，必须编译后才能运行。而python是集合了PHP和Java两者的优点，既是解释型语言，也是编译型语言（提高运行速度）。

## 1.3 Python的安装和运行

### 1.3.1 Python的安装
在官网下载安装包，笔者使用的是Windows环境，安装完为了在任何地方都能执行python命令，将 `$PYTHON_HOME/bin` 添加到系统环境变量$PATH里。

### 1.3.2 Python的运行
Windows环境下，双击.py文件可以运行python程序，但是会闪退，作为程序员一般不会这么干，为了提高逼格建议打开CMD，用命令 python xxx.py 运行程序。另外，双击.py文件大多数情况下是为了查看源码，可以选中一个.py文件，右键选择打开文件的默认程序，笔者选的是Sublime，Notepad++等其他编辑器也是不错的选择。

## 1.4 Python的实现版本
- Python 的标准实现是使用 C 语言完成的 （也就是 CPython），所以要使用 C 和 C++ 编写 Python 扩展；
- Python 的 Java 实现被称作 Jython，要使用 Java 编写其扩展；
- Python 的 C#  实现被称作 IronPython，是针对 .NET 或 Mono 平台的实现，可以使用 C# 或者 VB.Net 扩 展 IronPython。

# 练习
Python 执行程序的安装位置和标准库模块的安装位置：
笔者安装的Python版本是2.7.8，安装目录是D:\Python27，执行程序的位置就是 D:\Python27\python.exe

标准库模块的安装位置：D:\Python27\Lib，通过 `python -v` 进入python命令行模式时，可以看到python启动时导入的模块和模块路径，这些模块大部分位于D:\Python27\Lib 下。
