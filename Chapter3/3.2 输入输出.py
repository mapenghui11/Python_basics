# 输入

a = input()
# 直接从键盘上接收一个值并赋值给变量a
b = input('请输入一个数字：')
# 从键盘上接收一个字符串类型的值赋值给b,在屏幕上将接收的字符串作为提示信息显示

# 输出
c = 'hello'
d = 'world'
print(c, end='')  # end=''表示取消print函数的自动换行
print(d)

print(c, end='***')
# 输出为 hello***，在未指定end情况下，print函数会z自动以换行符‘\n’作为结束

print(c, d, c, sep='***')
# 输出为 hello***world***hello，设置sep函数的值来作为分隔符

# 格式化输出：format()函数
e = 'python'
f = '数据分析'
g = '零基础'
print('这是一本关于{}及{}的书，适合{}的人群学习'.format(e, f, g))
# 字符串里的{}分别与3个参数按顺序对应
print('这是一本关于{1}及{0}的书，适合{2}的人群学习'.format(e, f, g))
# {0}对应format函数的第1个参数，以此类推按位置对应
print('这是一本关于{x}及{y}的书，适合{z}的人群学习'.format(x=e, y=f, z=g))
# 自由指定别名
print(f'这是一本关于{e}及{f}的书，适合{g}的人群学习')
# 两种函数结合的特殊方法，f在开头代替format



