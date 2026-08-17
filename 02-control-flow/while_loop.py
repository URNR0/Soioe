# while_loop.py — Lesson 2 while 循环
# 对照 C:while 的写法和 C 几乎一样,但同样用「冒号 + 缩进」而不是 { }
# 没有 i++ / i--,要用 i += 1 / i -= 1

# 1. 基本 while:打印 1 到 5
i = 1
while i <= 5:
    print(i)
    i += 1          # 注意:Python 没有 i++,要写 i += 1

# 2. break:提前跳出循环(和 C 一样)
n = 0
while True:         # while True 相当于 C 的 while(1)
    n += 1
    print(n)
    if n >= 3:
        break       # 到 3 就停

# 3. continue:跳过本轮剩下的,进入下一轮
j = 0
while j < 5:
    j += 1
    if j == 3:
        continue    # 跳过 3,不打印它
    print(j)

# 4. while-else:C 里没有!当循环「正常结束」(没被 break)时才执行 else
k = 1
while k <= 3:
    print(k)
    k += 1
else:
    print("循环正常结束,没有 break")
