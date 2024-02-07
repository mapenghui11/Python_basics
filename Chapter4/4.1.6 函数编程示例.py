# 求出半径为2、4、6、... 、28、30的15个圆的平均面积，将结果四舍五入并保留两位小数
import math


def area(r):
    ave_area = math.pi * r * r
    return ave_area


sum_1 = 0
count = 0
for i in range(2, 31, 2):
    sum_1 = sum_1 + area(i)   # 先定义一个求圆面积的函数，在循环调用这个函数
    count = count + 1
result = round(sum_1/count, 2)
print(f"{count}个圆的平均面积为{result}")


# 从键盘上接收1个字符串，并统计这个字符串里大小写字母有多少个
def count_number(str):
    count_upper = 0
    count_lower = 0

    for i in str:
        if i.isupper():
            count_upper = count_upper + 1
        elif i.islower():
            count_lower = count_lower + 1
        else:
            pass

    return count_upper, count_lower


input_str = input("请输入一个字符串：")
count_upper, count_lower = count_number(input_str)
print(f"{input_str}的大写字母有{count_upper}个，小写字母有{count_lower}个")


