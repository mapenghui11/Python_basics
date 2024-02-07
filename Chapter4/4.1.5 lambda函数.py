"""
lambda函数：通过关键字lambda声明，不需要定义函数名称，
          函数体以单个简单的表达式存在，包含if-else语句，但不能包含循环语句、return语句，
          会自动将表达式结果返回
"""

sum_1 = lambda x, y: x + y   # x, y是lambda函数的参数，x + y是表达式
print(sum_1(2, 4))           # 调用sum函数

# lambda函数的使用方法总结
value_1 = lambda x, y: x + y
print(value_1(2, 3))               # 参数是x, y,返回x + y的值

value_2 = lambda: 10 + 6
print(value_2())                   # 没有参数，返回10 + 6的值

value_3 = lambda *args: args       # 参数个数不限，为不定长参数，将所有参数组合成一个元组后返回
print(value_3(1, 2, 3, 4, 5))

value_4 = lambda **kwargs: kwargs  # 同样为不定长参数，结合关键字参数使用，将关键字作为键，参数值作为值组合成字典后返回
print(value_4(a=1, b=2))

value_5 = lambda x, y: x if x > y else y
print(value_5(1, 2))               # 参数是x, y，若x大于y则返回x，否则返回y