# 可变与不可变数据类型

# 数字、字符串、元组为不可变数据类型对象：属性值改变则地址属性改变，产生一个新对象
a = 1
print(a, id(a), type(a))
a = 2
print(a, id(a), type(a))
'''
以数字举例，
输出为1 140712009134888 <class 'int'>  
     2 140712009134920 <class 'int'>
'''
# 列表、字典、集合为可变数据类型对象：属性值改变但地址属性不发生改变，不会产生一个新对象
b = [1, 2, 3]
print(b, id(b), type(b))
b[0] = 100
print(b, id(b), type(b))
'''
以列表举例，
输出为[1, 2, 3] 3082528543488 <class 'list'>
     [100, 2, 3] 3082528543488 <class 'list'>
'''

# 数据类型转换
c = 520
print(type(c))
c = float(520)  # 将整数c转换成浮点型
testResult = isinstance(c, float)  # 通过isinstance()函数判断是否成功转换，是则返回True
print(testResult)
