# function_basics.py — 函数:把代码封装成可复用的块
def greeting(name):
    print(f"你好,{name}~")
greeting("URNR")

def add(a, b):
    return a + b
result = add(3, 5)
print(result)  # 输出: 8


# 返回多个值(实际是返回一个 tuple,靠解包接收)
def get_info():
    return "URNR", 20
name, age = get_info()
print(name, age)  # 输出: URNR 20

# 默认参数:调用时不传,就用默认值
def say(name, greeting="你好"):
    print(f"{greeting},{name}")

say("URNR")                # 默认"你好"
say("URNR", "早上好")       # 覆盖默认值

# 1
def square(n):
    return n * n
print(square(5))  # 输出: 25
# 2
def receive(a, b):
    return a + b, a - b
total, diff = receive(10, 3)
print(total, diff)
# 3
def power(base, exp=2):
    return base ** exp
print(power(3))
print(power(3, 3))

