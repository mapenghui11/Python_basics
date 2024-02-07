# break语句：强制跳出整个循环，与break语句属于同一代码块且位于break语句后的代码将不被执行

# while循环的break语句
count = 1
while True:
    count = count + 1
    if count == 5:
        break
print(f"在第{count}次循环通过break强制跳出循环")
# for循环的break语句
for i in ['p', 'y', 't', 'h', 'o', 'h']:
    if i == 't':
        break
print(f"在i=='t'时通过break强制跳出循环")

# continue语句：不再执行当前循环，直接进入下一次循环
count = 1
for i in ['p', 'y', 't', 'h', 'o', 'h']:
    if i == 't':
        print(f"不执行第{count}次循环，遇到continue语句")
        count = count + 1
        continue
    print(f"执行了第{count}次循环")
    count = count + 1

# else语句
'''
如果循环体没有break语句，循环结束后会执行else里的代码块，
若有break语句，循环强制结束后不会执行else里的代码块
'''

# pass语句
'''
pass语句代表空语句，什么都不做
'''