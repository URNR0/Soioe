point = (3, 5)
print(point[0])     # 索引,和 list 一样
print(point[-1])
print(len(point))
x, y = point            # 解包 unpacking:一次性拆成两个变量
print(x, y)

# 先跑上面,然后把下面这行的 # 删掉,再跑一次,看看会发生什么:
# point[0] = 10         # ← 会报 TypeError!tuple 不可变

message = (1999, 12, 25)
year, month, day = message
print(year, month, day)
for i in message:
    print(i)
#message[0] = 2000