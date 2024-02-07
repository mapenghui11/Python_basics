"""
字典:字典用一对{}表示，{}中存放元素，元素由键和值组成，
每个元素之间用逗号隔开，元素的语法格式为"键:值",
键是不可变数据类型，同一字典的键是唯一的，但是值可以重复
"""

# 字典的创建

# 直接创建字典
firstDict = {'0': 'hello', '1': 'python'}
firstDict1 = {'hello': '0', '99': '1', '(1,2)': 5}  # 键可以是数字、字符串、元组
# 使用dict()函数创建字典
secondDict = dict(hello=0, python=1)  # 代表以hello和python为键，数字1和2为对应值的字典
# 使用dict()函数与列表联合创建字典
dictList = [('hello', 0), ('python', 1)]  # 创建一个元素为二元组形式的列表
thirdDict = dict(dictList)                # 将列表传入dict()函数
# 使用dict()函数与zip()函数联合创建字典
dictKey = ('hello', 'python', 520)   # 定义要传入zip()函数的键,键是不可变数据类型,所以为元组类型
dictValue = [0, 1, 'python']         # 定义要传入zip()函数的值
fourthDict = dict(zip(dictKey, dictValue))  # 将zip()函数传入dict()函数

dictKey1 = 'xyz'    # dictKey也可以是字符串
dictValue1 = [0, 1, 2]
fourthDict1 = dict(zip(dictKey, dictValue))
# 使用字典推导式创建字典
fifthDict = {i: i**2 for i in range(1, 6)}

# 字典的访问
dict1 = {'a': 'hello', 'b': 'python'}
print(dict1['a'])      # 通过键找到对应的值进行访问
print(dict1.get('a'))  # 通过get()函数返回键对应的值
print(dict1.get('c', None))  # 若指定键不存在对应值，则返回None
print(dict1.items())   # items()函数返回字典所有的键值对
print(dict1.keys())    # keys()函数返回字典所有的键
print(dict1.values())  # values()函数返回字典所有的值

dict2 = {'a': 'hello', 'b': 'python'}  # 遍历字典的每个元素
for key, value in dict1.items():
    print(key, value)


# 字典元素的增删改操作
dict_a = {0: 'hello', 1: 'python'}

dict_a[2] = 'i love'   # 通过’字典名[键]=值‘添加元素
dict_a[1] = 'world'    # 修改字典元素，应传入字典中原本存在的键
del dict_a[0]          # 删除字典中键0对应的元素
value = dict_a.pop(1)  # pop(key)函数可以删除key键对应的元素，并返回该键对应的值
print(value)
dict_a.clear()         # 清空字典的所有元素，让字典为空
del dict_a             # 删除整个字典

# 字典对象的常用方法
dict_1 = {0: 'hello', 1: 'python'}
dict_2 = {0: '1 love', 2: 'python'}

dict_1.update(dict_2)
print(dict_1)
'''
输出为{0: '1 love', 1: 'python', 2: 'python'}，
以字典dict_2的键值对为基础，更新dict_1的键值对，
若有相同键，则更新dict_1对应键的值，若无相同键，则为dict_1添加新的键值
'''
dict_1.copy()  # 返回一个字典的浅复制
dict_1.popitem()  # 删除字典中最末端的元素，并以二元组的形式返回该元素
dict_3 = dict_1.fromkeys((1, 2, 3), (4, 5))  # 以(1, 2, 3)中的序列作为键，(4, 5)元素整体作为值创建一个新字典
len(dict_1)  # 返回字典的元素数量
str(dict_1)  # 将字典类型转换成字符串类型

