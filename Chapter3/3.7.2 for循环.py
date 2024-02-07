"""
按照序列中元素的排列顺序，依次遍历序列中的所有元素，
并把对应的元素赋值给变量进行储存，所有元素变量完成后退出循环
"""

# 遍历字符串(遍历列表、元组、集合序列与遍历字符串没有区别)
str_1 = 'abcdef'
n = 1
for i in str_1:
    print(f"第{n}次循环：i={i}")
    n = n + 1

# 多变量for循环
tupleList = [(1, 2), (3, 4), (5, 6)]
m = 1
for i, j in tupleList:
    print(f"第{m}次循环：i={i}, j={j}")
    m = m + 1

# 遍历字典序列：item()函数
dict_1 = {1: 'a', 2: 'b', 3: 'c'}
k = 1
for i, j in dict_1.items():
    print(f"第{k}次循环：i={i}, j={j}")
    k = k + 1

# for循环结合range()函数

# range()函数只传入一个参数
for i in range(3):     # range(3)生成0、1、2的数字序列
    print(f"第{i+1}次循环：i={i}")
# range()函数只传入三个参数
for i in range(2, 8, 2):     # range(2, 8, 2)生成2到7的数字序列，步长为2，不设置步长参数默认为1
    print(f"第{i//2}次循环：i={i}")
# range函数的类型转换
rangeList = list(range(8))    # 通过list()函数将range(8)返回值转换成列表
rangeTuple = tuple(range(8))  # 同理
rangeSet = set(range(8))

# for循环与enumerate()函数结合使用
enList = ['hello', 'i love', 'python']
for i, j in enumerate(enList):
    print(f"索引{i}的对应值：{j}")
'''
输出为：索引0的对应值：hello
      索引1的对应值：i love
      索引2的对应值：python
enumerate(seq[, start])函数可以将序列seq的索引和对应值结合起来，
序列seq通常是字符串、列表、元组、集合，
start代表索引的起始位置，默认为1
'''

# for循环与zip()函数结合使用
List_1 = ['hello', 'i love', 'python']
List_2 = ['你好', '我爱', '编程']
m = 1
for i in zip(List_1, List_2):
    print(f"第{m}次循环:{i}")
    m = m + 1
'''
输出为：第1次循环:('hello', '你好')
      第2次循环:('i love', '我爱')
      第3次循环:('python', '编程')
zip(seq_1, seq_2, ...)函数可以将两个或两个以上序列的元素对应组合成元组
'''