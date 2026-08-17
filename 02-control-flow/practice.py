# practice.py — Lesson 2 练习:把 if 和循环结合起来
# 复习时先自己想想结果,再运行看输出

# 1. FizzBuzz 经典面试题:
#    1~15,能被 3 整除输出 Fizz,能被 5 整除输出 Buzz,都能整除输出 FizzBuzz,否则输出数字
for n in range(1, 16):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# 2. 求 1 加到 100 的和
total = 0
for i in range(1, 101):
    total += i
print("1 加到 100 =", total)

# 3. 九九乘法表(嵌套循环:for 里再套 for)
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j}", end="  ")  # end="  " 打印后不换行,换成两个空格
    print()          # 每一行结束再换行
