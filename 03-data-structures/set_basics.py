# set_basics.py — 集合:无序、不重复
fruits = {"apple", "banana", "cherry", "apple"}  # 故意放两个 apple
print(fruits)               # 观察apple个数
print(len(fruits))          # 3,不是 4(重复的被自动去掉)
fruits.add("orange")        # 新增元素
print(fruits)
print("banana" in fruits)
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # 并集
print(a & b)  # 交集
print(a - b)  # 差集

num = {1, 2, 2, 3, 5, 6, 7}
print(len(num))
num.add(4)
num.remove(1)
print(1 in num)
num2 = {5, 6, 7, 8, 9}
print(num | num2)
print(num & num2)