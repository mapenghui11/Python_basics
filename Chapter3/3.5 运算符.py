# 算术运算符

# + 加法
print('a' + 'b')
print([1, 2] + [3, 4])
print((1, 2) + (3, 4))  # 可以用于数值加法运算或同一数据类型间的拼接操作
# - 减法：只用于数值减法运算
# * 乘法
str1 = 'ab'
print(str1 * 3)     # 输出‘ababab’，可以用于数值乘法运算和字符串，字符串只能乘以数字
# / 除法
# // 向下取整
print(5 // 2)  # 两个数字类型相除后，向下取最接近于商的一个整数
# ** 幂
# % 取余数

# 比较运算符

# == 比较两个对象是否相等
# != 比较两个对象是否不相等
# > >= < <=

# 逻辑运算符
a = False
b = True
# and : 只有a和b都为True时，a and b才为True
# or : 只要a和b中有一个为True, a or b就为True
# not : a为True时，not a为False,a为False时，not a为True
'''
通常情况下，默认0、” “、()、{}、[]、None都是False,
剩余的所有数字和字符串都是True
'''

# 位运算符

# 赋值运算符

# 成员运算符
# in : x in y,若x在序列y中返回True,否则为False
# not in : x not in y,若x不在序列y中返回True,否则为False

# 身份运算符
# is : x is y,两个变量的对象地址相同则返回True,否则返回False
# not is : x not is y,两个变量的地址不相同则True,否则False