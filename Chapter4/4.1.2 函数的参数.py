"""
形参：若想调用某个函数，必须传入个数与该函数参数列表中形参个数相同多的参数值，
     传入的参数值将按形参顺序一一赋值给形参
实参：指函数调用时传入形参的参数值
"""


def f(x, y):
    z = x + y
    return x, y, z


x, y, z = f(10, 20)
print(f"x={x}, y={y}, z={z}")
'''
f(x, y)函数的形参为x, y,形参个数为2，
则调用f(x, y)函数需要2个参数值(否则会报错)，
参数值传入后将依次赋值给2个形参，即将参数值10赋值给给x，参数值20赋值给给y
'''


def length(str_1):
    sum_1 = 0
    for i in str_1:
        sum_1 = sum_1 + 1
    return sum_1


str_1 = 'i love python'
length = length(str_1)  # 调用函数并传入参数值
print(f"{str_1}的长度为{length}")