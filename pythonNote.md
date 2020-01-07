# Python Note

## 1.I/O
   ``` python
   print('string1','string2',…) # 输出字符串，每个字符串之间会加一个空格输出{{{
   print('I\'m ok.') # 用反斜杠作为转义符号
   print(r'\\\n\\') # 用r'content'来标识不转义
   print('''line1
   ... line2
   ... line3''')
   # 用'''...'''表示多行内容,...不是代码，在.py文件中不用写,多行字符串也可用前面加r来不转义
   
   var = input('prompt text')
   # 输入字符串，用var变量存起来，输入前有提示字符串'prompt text'输出
   # input()输入的是字符串，如需数字比较需要用int()来转换字符为数字类型}}}
   ```

## 2.注释与格式
   ``` python
   # notes content: # 注释以#开始，以：结束
   Python使用缩进组织代码块，坚持用4个空格缩进
   Python中用：来结束一个保留字语句
   ```

## 3.变量与基本运算
   ``` python
   一种除法是‘/’计算结果是浮点数，即使整除也是浮点数
   一种除法是‘//’两个整数除法仍然是整数
   ```

## 4.字符串
   ``` python
   ord() # 获取字符的整数表示 例：>>>ord('A') 65
   chr() # 编码转化为对应字符 例：>>>chr(66) 'B'
   
   >>>'\u4e2d\u6587' '中文' # 用16进制写
   
   >>>'ABC'.encode('ascii') b'ABC' 用ascii编码英文为bytes
   >>>'中文'.encode('utf-8') b'\xe4\xb8\xad\xe6\x96\x87' 用utf-8编码中文bytes
   
   >>>b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') '中文' 解析字节
   >>>b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore') '中'
   传入errors='ignore'忽略解析时部分无效字节
   
   >>>len('ABC') 3 >>>len('中文') 2 # 计算包含了多少个字符
   
   >>>'hello, %s' % 'world' 'hello, world'
   >>>'hi, %s, you have $%d.' % ('Li',1000) 'hi, Li, you have $1000'
   # 格式化占位符	占位符:	%d (整数) %f (浮点数) %s (字符串) %x (十六进制整数)
   >>>print('%03d,%.2f' % (3,3.1415926)) 003 3.14
   # 占三个字符，用0补全。取小数点后两位。其中%要用%%转译
   
   >>>'hello, {0},成绩提升了 {1:.1f}%'.format('小明',17.125) 
   'hello, 小明, 成绩提升了 17.1%'
   # 用format()格式化字符串。其中的%不用转译
   
   >>>a = 'abc'
   >>>b = a.replace('a', 'A')
   # 变量a中还是'abc',而.replace()方法是对字符串'abc'操作，创建一个新的字符串返回给b
   ```

## 5.列表list
   ``` python
   >>>classmates = ['person1', 'person2', 'person3'] # 创建一个classmates列表
   >>>classmates # 输入列表名可输入列表内容： ['person1', 'person2', 'person3']
   >>>len(classmates) # 用len()获取列表元素个数
   >>>classmates[0] # 通过索引可访问元素内容：'person1'
   >>>classmates[-1] # 可通过传递-1参数访问最后一个元素，也可从后方向前访问
   >>>classmates.append('person4') # 可通过.append()向列表添加元素
   >>>classmates.insert(1,'person1.5') # 可通过.insert()想列表插入元素
   >>>classmates.pop() # 可通过.pop()删除列表尾部元素
   >>>classmates.pop(1) # 可通过.pop() 传参删除指定元素
   >>>classmates[1] = 'people' # 可通过索引直接给对应元素赋值
   # 列表中元素可以是不同类型.也可以是list类型,组成多维列表
   
   >>>a = ['c', 'b', 'a']
   >>>a.sort()
   # .sort()对list内容进行排序,改变了list中的元素顺序
   ```

## 6.元组Tuple
   ``` python
   >>>t = (1,2) # 创建一个t元组
   >>>t = (1,) 创建一个只有一个元素的元组，用逗号来区别数字1
   # 元组元素不可变，但是可以放入列表元素，让列表来变达到安全灵活的目的
   ```

## 7.判断
   ``` python
   >>>if x:
   >>>    print('trueX')
   >>>elif y:
   >>>    print('trueY')
   >>>else:
   >>>    print('false')
   # 条件后面要加冒号，当一个if满足条件后，后面的else或elif都不执行
   ```

## 8.循环
   ``` python
   >>>sum = 0
   >>>for x in range(101): # range（101）可以创建出一个从0到100的一个列表
   >>>    sum = sum + x 
   >>>print(sum)
   # for in : 循环，将in后的列表或元组依次取出赋给for后的变量
   >>>while n > 0:
   # while : 循环 ，只要满足条件就不断循环
   # python 支持break和continue操作
   ```

## 9.字典dict无序无重复元素集合set
   ``` python
   >>>d = {'name1':95,'name2':75,'name3':85} # 键值存储
   >>>d['name1'] = 90 # 通过键值访问修改
   >>>'name4' in d # 通过in判断key是否存在
   >>>d.get('name4') # 当key不存在时，返回None
   >>>d.get('name4',-1) # 当key不存在时，返回指定的-1
   >>>d.pop('name1') # pop()方法删除指定的键值,没找到键值会异常KeyError
   >>>s1 = set([1,2,3])
   >>>s2 = set([2,3,4])
   >>>s1 & s2 # 交集
   >>>s1 | s2 # 并集
   >>>s1.add(5) # 添加key值5,不可添加list,TypeError:unhashable type: 'list'
   >>>s1.remove(5) # 删除key值5
   # 集合（set）类型，不可以用下表索引，TypeError:'set' object is not subscriptable
   ```

## 10.函数
   ``` python
   >>>abs(-100) 100
   >>>hex(255) 0xff
   >>>int('123') 123
   >>>float('12.34') 12.34
   >>>str(1.23) '1.23'
   >>>bool(1) 'true'
   # 内置函数 见：http://docs.python.org/3/library/functions.html
   
   >>>a = abs
   >>>a(-1)
   # 函数名 是	指向一个函数对象的引用。可将函数名赋给一个变量,起别名
   ```

   - **定义函数**
      ``` python
      >>>def function_name (argument):
      ...    return None
      # 定义用def 函数名 括号 参数 冒号 最后用return返回参数
      
      >>>from file_name import my_def_function_name
      # 在文件的当前目录下启动python导入自定义的函数
      
      >>>def nop():
      ...    pass
      # 空函数，用pass可以让程序线运行起来，不会出现语法错误
      
      >>>if not isinstance(x, (int, float)):
      ...    raise TypeError('bad operand type')
      # 用内置函数isinstance()检查变量类型，用raise抛出异常
      
      >>>import math # math.sqrt() math.sin() math.cos()
      ...def move(x,y,step,angle):
      ...    return x+step*math.cos(angle) , y+step*math.sin(angle)
      >>>x, y = move(100, 100, 60 ,math.pi/6)
      >>>print(x, y) //151.96152422706632 70.0
      >>>r = move(100, 100, 60 ,math.pi/6)
      >>>print(r) //(151.96152422706632, 70.0)
      # 返回多参数，实际上是返回一个元组，只不过元组可以按位置分别赋值给变量
	  ```
		   
   - **函数参数**
      ``` python
      >>>def function_name (argument):
	  ```

      - **位置参数（positional argument）**

      - **默认参数 (default argument)**
	    ``` python
      	>>>def add_end(L=None)
      	...    if L is None:
      	...        L = []
      	...    L.append('END')
      	...    return L
        ```
		- None是不变对象，当调用一次默认参数后也不会改变
      	- 如果==默认参数是可变参数==，当调用一次默认参数==有可能==改变默认参数内容
      	- 用==None==或==str==这种==不变参数==来确保默认参数不会变

      - **可变参数（variable argument)-传递List**
	    ``` python
      	>>>def calc(*numbers):
      	...    sum = 0
      	...    for n in numbers:
      	...        sum = sum + n * n
      	...    return sum
        ```
        - 可以传入任意数量参数
        ``` python
        >>>calc(1,2) 5
        >>>nums = [1, 2, 3]
        >>>calc(*nums) 14
        ```
        - *nums 表示把nums中所有元素当作参数传进去

      - **关键字参数（keyword argument）-传递Dict**
	    ``` python
      	>>>def person(name, age, **kw):
      	...    print('name:', name, 'age:', age, 'other:', kw)
        ```
        - 关键字参数目的是为了传入含参属名的参数，即一个dict
        ``` python
      	>>>extra = {'city': 'Beijing', 'job': 'Engineer'}
      	>>>person('Jack', 24, **extra) 
        ```
        - name: Jack age: 24 other:{'city': 'Beijing', 'job': 'Engineer'}
        - **extra是把extra中的键值复制一份，传入给kw,改动kw，不会影响extra

      - **命名关键字参数（named keyword parameter）**
        - *后的参数为 命名关键字参数
	    ``` python
      	>>>def person(name, age, *, city, job):
      	...    print(name, age, city, job)
        ```

		``` python
      	>>>person('Jack', 24, city = 'Beijing', job = 'Engineer')
        # Jack 24 Beijing Engineer
        ```

        - 如果定义中已经有了可变参数，后面的命名关键字就不需要*了
        - 同样的命名关键字也可以用默认参数
		``` python
      	>>>def person(name, age, *args, city, job):
        ```

   - **递归函数**
      - **尾递归：** 在函数返回时，调用自身，且return语句不能包含表达式
      - python 没有对尾递归做优化，任何递归函数都会出现栈溢出
	  ``` python
      RecursionError: maximum recursion depth exceeded in comparison
	  ```
      - **汉诺塔（hanoi）**
	  ``` python
      def move(n, a, b, c):
      	if n == 1:
      		print(a, '-->', c)
      	else:
      		move(n-1, a, c, b) # n-1个从a到b
      		move(1, a, b, c) # 把最下面一个从a到c
      		move(n-1, b, a, c) # 把n-1个从b到c
      # test:
      move(3, 'A', 'B', 'C')
      ```
## 11.切片
   - list，tuple，string 都可用切片来取
      ```python
      >>>L = ['person1', 'person2', 'person3', 'person4', 'person5'] #list
      >>>T = ('person1', 'person2', 'person3', 'person4', 'person5) #tuple
      >>>S = 'ABCDEFG' #string
   
      >>>L[0:3] #正切片,取下标0，1， 2
      ['person1', 'person2', 'person3]
      >>>L[-2:] #倒切片,取下表倒数第二，倒数第一
      ['person4', 'person5]
      >>>L[-2:-1] #倒切片，取下标倒数第二
      ['person4']
      >>>L[::2] #每两个取一个
      ['person1', 'person3', 'person5']
      ```

## 12.迭代Iteration
   ``` python
   >>>d = {'a': 1, 'b': 2, 'c': 3}
   >>>for key in d: #访问dict键值
   >>>    print(key)
   >>>for value in d.values(): #访问dict值
   >>>    print(value)
   >>>for key, value in d.items(): #访问dict键值和值
   >>>    print(key,value)
   >>>for ch in 'ABC' #迭代字符串
   >>>    print(ch)
   ```

   - enumerate()方法可以将list变成索引元素对
      ``` python
      >>>for i, value in enumerate(['A', 'B', 'C']):
      ```
   
   - 判断是否可迭代
      ``` python
      from collections import Iterable #导入collections模块的Iterable类型
      >>>isinstance('abc', Iterable) #string是否可迭代
      True
      >>>isinstance(123, Iterable) #整数是否可迭代
      False
      ```

## 13.列表生成式List Comprehensions
   - 列表生成式，要把生成元素x * x放到前面，后跟for循环,可加判断
      ``` python
      >>>[x * x for x in range(1, 11) if x % 2 ==0]
      [4, 16, 36, 64, 100]
      ```
   
   - 用双循环生成全排列
      ``` python
      >>>[m + n for m in 'ABC' for n in 'XYZ']
      >>>['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
      ```

   - 用两个变量生成list
      ``` python
      >>>d = {'x': 'A', 'y': 'B', 'z': 'C'}
      >>>[k + '=' + v for k, v in d.items()]
      ['y=B', 'x=A', 'z=C']
      ```
   
   - 将list中所有字符串变成小写
      ``` python
      >>>L = ['Hello', 'World', 'IBM', 'Apple']
      >>>[s.lower() for s in L]
      ['hello', 'world', 'ibm', 'apple']
      ```
   
   - 利用os模块列出文件和目录
      ``` python
      >>>import os 
      >>>[d for d in os.listdir('.')]
	  ```

## 14.生成器generator
   ``` python
   >>>g = (x * x for x in range(10))  # 注意这里用的是小括号存储的for不是中括号
   >>>for n in g:
   ...    print(n)
   # 创建generator，并打印它
   >>>next(g)
   # 也可以用next()函数推算g的下一个元素，g保存的是算法
   >>>g
   # <generator object <genexpr> at 0x0357EDF0>
   # g存储的是算法，用for或者next来让算法进行下去
   ```
   - 一个函数定义中包含yield关键字，这个函数就是一个generator
   - 每次函数执行到yield就会返回停止，下次再从停止的地方继续执行
   
   - for循环拿不到generator的return语句的返回值
   - 必须捕获StopIteration错误，返回值在StopIteration的value中

## 15.迭代器iterator
   - 凡是可用作于==for循环的对象==都是==Iterable==类型，如list,tuple,dict,set,str
   - 凡是可作用于==next()函数==的对象都是==Iterator==类型，如generator,带有yield函数
   
   - 数据集合list,dict,str等可通过==iter()函数==获得Iterator对象
   
   - for循环的本质就是不断调用next()函数实现的
   ``` python
   it = iter([1, 2, 3, 4, 5]) #首先获得Iterator对象
   while True: #循环
       try
           x = next(it) #获得下一个值
       except StopIteration:
           break
   ```

## 16.高阶函数Higher-order function
   - 变量可以指向函数
      ``` python
      >>>f = abs
      >>>f(-11)
      11
      ```
	  - abs(-11)是函数调用，abs是函数本身

   - 函数名也是变量名
      - 注：由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向在其它模块也生效，要用import builtins; builtins.abs = 10。

   - 传入函数
      - 既然变量可以指向函数，函数的==参数能接收变量==，那么一个函数就可以接收另一个==函数作为参数==，这种函数就称之为高阶函数。
      ``` python
	  def add(x, y, f):
		  return f(x) + f(y)
      # test：
      x = -5
      y = 6
      f = abs
      f(x) + f(y) ==> abs(-5) + abs(6) ==> 11
      return 11
	  ```

   - 高阶函数 **map(f, [,,...])**
      - 第一个参数f是函数，第二个参数list中每个元素，用f函数计算一遍，返回生成的结果Iterator，要用list()转换成list使用
	  ``` python
	  >>> list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
	  ```

   - 高阶函数 **reduce(f, [,,...])**
      - 第一个参数f是函数，第二个参数list中从左到右，每两个用f函数计算，结果与下一个进行f函数计算
	  ``` python
	  # 求和
	  >>> from functools import reduce
      >>> def add(x, y):
      ...     return x + y
      ...
      >>> reduce(add, [1, 3, 5, 7, 9])
      25

	  # string 转换 int
	  from functools import reduce

      DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
      
      def char2num(s):
          return DIGITS[s]
      
      def str2int(s):
          return reduce(lambda x, y: x * 10 + y, map(char2num, s))
      ```

   - 高阶函数 **filter(f, [,,...])**
      - 把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。f是一个判断函数返回TorF
	  ``` python
	  def is_odd(n):
		  return n % 2 == 1
      # test:
	  list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7]))
	  # [1, 3, 5, 7]

	  # ===用filter求素数===
	  def _odd_iter(): # 构造一个奇数序列
      n = 1
      while True:
          n = n + 2
          yield n

      def _not_divisible(n): # 定义一个筛选函数
      return lambda x: x % n > 0

	  def primes(): # 定义一个生成器，不断返回下一个素数
      yield 2
      it = _odd_iter() # 初始序列
      while True:
          n = next(it) # 返回序列的第一个数
          yield n
          it = filter(_not_divisible(n), it) # 构造新序列

      # 打印1000以内的素数:
      for n in primes():
          if n < 1000:
              print(n)
          else:
              break
      # ===End 用filter求素数===

   - 高阶函数 **sorted([,,...], key=f, reverse=True)**
      - 用于排序，f定义排序前对每个元素做的处理，reverse为True则从大到小，默认从小到大

## 17. 返回函数
   - 函数作为结果值返回
      ``` python
	  def lazy_sum(*args):
          def sum():
              ax = 0
              for n in args:
                  ax = ax + n
              return ax
          return sum
      # test:
	  >>> f = lazy_sum(1, 3, 5, 7, 9)
      >>> f
      <function lazy_sum.<locals>.sum at 0x101c6ed90>
	  >>> f()
      25
      ```
	  - 我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都==保存在返回的函数中==，这种称为 ==“闭包（Closure）”== 的程序结构拥有极大的威力。

   - 用闭包来延迟计算发生
      - 注：返回闭包时牢记一点：==返回函数==不要引用任何==循环变量==，或者==后续会发生变化==的变量。
	     ``` python
	     def count():
             fs = []
             for i in range(1, 4):
                 def f():
                      return i*i
                 fs.append(f)
             return fs
       
         f1, f2, f3 = count()
	     ```
      - 再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
         ``` python
         def count():
             def f(j):
                 def g():
                     return j*j
                 return g
             fs = []
             for i in range(1, 4):
                 fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
             return fs
         ```

## 18. 匿名函数 lambda
   - 匿名函数赋值给一个变量，再利用变量来调用该函数：
      ``` python
	  >>> f = lambda x: x * x
      >>> f
      <function <lambda> at 0x101c6ef28>
      >>> f(5)
      25
	  ```
   - 匿名函数作为返回值返回：
      ``` python
      def build(x, y):
      return lambda: x * x + y * y
	  ```

## 19. 装饰器 Decorator
   - 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
   - 例如：在函数调用前后自动打印日志，但又不希望修改now()函数的定义
      ``` python
	  >>> def now():
      ...     print('2015-3-25')
      ...
      >>> f = now
      >>> f()
      2015-3-25
      # 函数对象有__name__属性
	  >>> now.__name__
      'now'
      >>> f.__name__
      'now'
	  ```

   - 本质上，decorator就是一个返回函数的高阶函数 
      ``` python
	  # 无参数decorator
	  import functools

      def log(func):
          @functools.wraps(func)
          def wrapper(*args, **kw):
              print('call %s():' % func.__name__)
              return func(*args, **kw)
          return wrapper
      
	  @log
	  def now():
		  print('2015-1-1')

      # 有参数decorator
	  import functools

      def log(text):
          def decorator(func):
              @functools.wraps(func)
              def wrapper(*args, **kw):
                  print('%s %s():' % (text, func.__name__))
                  return func(*args, **kw)
              return wrapper
          return decorator
      
	  @log('execute')
	  def now():
		  print('2015-1-1')
      ```

## 20. 偏函数 PartialFunction
   - functools.partial(f, *args, **kw)
      - f为函数，后面跟着需要固定的参数
	  ``` python
	  >>> import functools
      >>> int2 = functools.partial(int, base=2)
      >>> int2('1000000')
      64
	  # 相当于：
	  kw = { 'base': 2 }
      int('10010', **kw)
	  ```

## 21. 使用模块
   - python 模块标准格式
      ``` python
	  #!/usr/bin/env python3
      # -*- coding: utf-8 -*-
      
      ' a test module '
      
      __author__ = 'Michael Liao'
      
      import sys
      
      def test():
          args = sys.argv
          if len(args)==1:
              print('Hello, world!')
          elif len(args)==2:
              print('Hello, %s!' % args[1])
          else:
              print('Too many arguments!')
      
      if __name__=='__main__':
          test()
	  ```
      - 1 2行注释为直接在Unix/Linux/Mac上直接运行，和使用UTF-8编码
      - 任何模块代码的第一个字符串都被视为模块的文档注释
      - 使用__author__把作者名字写入
      - sys模块的argv变量中，用list存储了命令行的所有参数
      - argv至少有一个参数，因为第一个参数永远是py文件的名称
      - ==命令行==运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在==其他地方导入==该hello模块时，if判断将失败

   - 作用域
      - __xxx__这样的是特殊变量，可直接饮用，比如__name__存储函数名字
	  - _xxx和__xxx这样是private的

   - 默认情况下，Python解释器会搜索==当前目录==、==所有已安装的内置模块==和==第三方模块==，搜索路径存放在==sys模块==的==path变量==中：
      ``` python
	  # 查看包路径
	  >>> import sys
      >>> sys.path
	  ```
   - 添加自己的搜索路径：
      1. 直接修改**sys.path**，添加要搜索的目录
	     ``` python
		 >>> import sys
         >>> sys.path.append('/Users/my_py_scripts')
		 # 这种方法，运行后失效
		 ```
      2. 在系统中设置环境变量**PYTHONPATH**
	     - 只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响