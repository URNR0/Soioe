# for_loop.py — Lesson 2 for 循环(和 C 最大的不同!)
# 对照 C:C 的 for(i=0; i<n; i++) 是「数数」;
# Python 的 for 是「遍历」——挨个取出一个序列里的元素。想数数就用 range()

# 1. 遍历字符串:每个字符取出来
for ch in "Python":
    print(ch)

# 2. 遍历列表(后面会细讲,先当「一组东西」看)
for item in [10, 20, 30]:
    print(item)

# 3. 用 range()——相当于 C 的 for 循环
#    range(5) 生成 0,1,2,3,4(注意:不含 5,和 C 的 i<n 一样)
for i in range(5):
    print(i)

# range(起始, 结束):从 1 到 9
for i in range(1, 10):
    print(i)

# range(起始, 结束, 步长):打印偶数 0,2,4,6,8
for i in range(0, 10, 2):
    print(i)

# 4. 需要序号用 enumerate()
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 5. for-else:和 while-else 一样,没被 break 就执行 else
for i in range(3):
    print(i)
else:
    print("循环正常结束")
