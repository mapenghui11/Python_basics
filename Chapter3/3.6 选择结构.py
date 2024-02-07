# if 语句
x = input()
x = float(x)
if x < 100:
    print('x不能小于100')

# if-else语句
y = input()
y = float(y)
if y < 100:
    print('y不能小于100')
else:
    print('满足y大于100')

# if-elif-else语句
z = input()
z = float(z)
if z < 100:
    print('z不能小于100')
elif 100 <= z <= 150:
    print('满足z大于100且小于150')
else:
    print('满足z大于150')
'''
若所有if及elif后跟的条件表达式的返回值均为False，
则执行else代码块，执行完后跳出if-elif-else结构
'''