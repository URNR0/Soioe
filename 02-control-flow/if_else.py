# if_else.py — Lesson 2 条件判断 if / elif / else
# 没有小括号 ( ) 包住条件,也没有大括号 { } —— 用「冒号 : + 缩进」表示代码块
# 没有 else if,写成 elif
# 逻辑运算用 and / or / not,不是 C 的 && / || / !

# 1. if / else 的基本写法
age = 19
if age >= 18:
    print("成年")
else:
    print("未成年")

# 2. 多分支 elif(相当于 C 的 else if 链)
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 60:
    print("C")
else:
    print("D")

# 3. 组合条件:and / or / not
temperature = 28
is_raining = False
if temperature > 20 and temperature < 30 and not is_raining:   # and ≈ &&,not ≈ !
    print("适合出去玩")

day = "Saturday"
if day == "Saturday" or day == "Sunday":  # or ≈ ||
    print("周末啦")

# 4. 真值判断:非零数字、非空字符串都算 True
#    对比 C:Python 里任何值都能直接放进 if,不必写成 if x != 0
x = 5
if x:            # 等价于 if x != 0
    print("x 非零")

name = ""
if name:         # 空字符串是 False
    print("有名字")
else:
    print("名字是空的")
