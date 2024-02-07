"""
变量的作用域：变量的可访问范围，变量在代码中的位置不同，作用域也不同
当程序运行需要使用变量时，首先要在代码中找到该变量的位置，
    查找变量遵循”局部作用域、嵌套作用域、全局作用域、内建作用域“的顺序
在python中，模块、类、函数的声明会产生新的作用域，但条件、循环、异常捕捉语句则不产生新的作用域

全局变量：在函数外部，模块内部定义的变量
局部变量：在函数内定义的变量，只在函数内有效，函数外部无法访问
"""
# global关键字
name = 'hello python'  # 全局变量
print(f"全局变量的初始值：{name}")


def change():
    global name
    name = 'i love python'


change()
print(f"global重新声明并修改全局变量后的值为：{name}")
'''
在函数体内部能够访问全局变量但不能对其进行修改，
在函数内部给全局变量加上global关键字，就能修改全局变量的值了
'''


# nonlocal关键字
def outer():
    name = 'hello python'
    print(f"外部函数的初始值：{name}")

    def inner():
        nonlocal name
        name = 'i love python'
    inner()
    print(f"使用nonlocal关键字修改外层函数后的值为{name}")


outer()
'''
在内层函数中不可以对外层函数变量进行修改，
需要在内层函数使用nonlocal关键字
'''

