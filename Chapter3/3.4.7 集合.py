"""
集合：无序的不重复元素序列，
能够高效的删除序列的重复值
"""

# 集合的创建

a = {1, 3, 5, 7, 9}  # 用花括号定义
b = set()            # 用set()函数创建空集合，空集合不能用b = {}创建，{}实际是空字典

# 集合的特性
'''
无序性：集合输出的元素顺序不一定与创建时的顺序一致
互异性：集合输出的元素不具有创建时的重复的元素
'''

# 集合的基本操作
# ===集合元素的添加
A = {'a', 'b', 'c'}
A.add('d')           # 用add()函数增加1个元素
A.update([1, 2])     # 用update()函数增加2个元素
# ===集合元素的删除
B = {'a', 'b', 'c', 'd', 'e'}
B.remove('a')        # 删除指定元素
B.discard('b')       # 删除指定元素,删除不存在的元素不会报错
B.pop()              # 删除随机元素
B.clear()            # 清空集合所有元素，输出set()
# ===集合元素的修改
C = {'a', 'b', 'c'}
C.remove('c')            # 先删除元素，再添加元素以修改元素
C.add('e')
# ===集合元素的查询
D = {'a', 'b', 'c', 'd'}
D = list(D)
print(D[0])              # 使用list()函数将集合转换为列表，再进行索引查询
# ===集合的并集和交集操作
E = {'a', 'b', 'c'}
F = {'a', 'e', 'c'}
print(E | F)              # "|"符号取并集
print(E.union(F))         # union()函数取并集
print(E & F)              # "&"符号取交集
print(E.intersection(F))  # intersection()函数取交集
# ===集合的差操作
print(E - F)              # 返回在E中存在但在F中不存在的元素
print(E.difference(F))
# 重复元素的剔除
G = ['a', 'b', 'c', 'a']
G = list(set(G))          # 先转换为集合剔除重复元素再转换为列表
print(G)

# 集合的常用内置函数
set1 = {1, 2, 3, 4}
set2 = {1, 2}
set1_copy = set1.copy()  # 创建集合set1的副本
set1.issubset(set2)      # 判断set1是否为set2的子集
set1.issuperset(set2)    # 判断set2是否为set1的子集
set1.isdisjoint(set2)    # 判断两个集合是否包含相同的元素




