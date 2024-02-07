"""
内置函数filter(function, iterable):
能够将序列iterable里不符合function条件的元素过滤掉并返回符合条件的新序列，
函数的第1个参数function是一个完成条件判断的函数,对序列中的每个元素进行判断，
若符合条件就将该元素返回
"""


# 将列表中不能被3整除的元素过滤掉
def right(x):
    if x % 3 == 0:
        return x


result = filter(right, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(result))


# 自己定义一个具有filter函数功能的函数，返回值为列表
def new_filter(function, iterable):
    new_result = []
    for i in range(len(iterable)):     # 遍历序列的长度
        value = function(iterable[i])  # 让序列的每个元素进入函数进行条件判断
        if value != None:              # 若函数return出任何值，代表函数的返回值不为空，该元素满足条件判断
            new_result.append(a)       # 将该元素加入列表
    return new_result


def right(x):
    if x % 3 == 0:
        return x


new_result = new_filter(right, [1, 2, 3, 4, 5, 6, 7, 8, 9])  # 调用filter函数
print(new_result)
