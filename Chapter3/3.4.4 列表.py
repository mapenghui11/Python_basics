# 列表的创建

# 用中括号定义
a = [1, 2, 3, 4]
b = ['python', 5, ['hello', 'world', 123]]
# list()函数创建
b1 = list(('python', 5, ['hello', 'world', 123]))
'''
list()函数其实是将其他数据类型的对象转换成了列表对象，
所以list()内的序列用[]列表、()元组、{}集合 均可
'''
# 列表推导式创建
c = [i ** 2 for i in range(10)]

# 列表的访问

e = ['python', 5, ['hello', 'world', 123]]
print(e[2][0])
# 索引访问，输出为列表e[2]的第1个元素‘hello’
f = [1, 2, 3, 4, 5]
print(f[1:5:2])
# 切片访问，以步长为2在范围[1:5]内选择元素

# 列表的增删改操作
firstList = [1, 3, 5, 7, 9]

secondList = firstList + [99]  # 整数只能和整数相加，不能和字符串相加
del firstList[0:4]             # 切片删除索引0到3的元素
del secondList                 # 删除整个列表
firstList[:3] = []             # 将空列表赋值给列表切片，删除该列表切片
firstList[2:] = [99, 100]      # 通过给索引或切片赋值来替换列表中的元素

# 列表对象的常用方法
anyList = [1, 2, 3, 4, 5]

anyList.append(6)     # 在列表最后添加一个元素6，只能添加一个元素，且只能在最后
anyList.extend([99, 100])  # 将列表[99， 100]添加到anyList的末尾，是对原列表的延长
anyList.insert(4, 0)  # 在索引4对应的列表位置添加元素0
anyList.remove(1)     # 移除列表中的元素1
anyList.count(2)      # 输出元素2在列表中出现的次数
anyList.index(2)      # 输出元素2在列表中第1次出现的索引值
anyList.index(3, 1, 5)  # 输出元素3在列表索引1到4范围中第1次出现的索引值
anyList.reverse()     # 将列表元素顺序颠倒
anyList.sort(reverse=True)  # 不传入参数reverse表示将列表元素从小到大排序，传入参数则从大到小排序
newList = anyList.copy()  # 复制列表

# python内置的处理列表方法
len(anyList)   # 求列表元素总数
max(anyList)   # 求列表元素最大值
min(anyList)   # 求列表元素最小值


