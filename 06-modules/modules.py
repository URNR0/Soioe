# modules.py — 模块与导入:用 Python 自带(和别人)写好的代码
import math            # 导入整个 math 模块
import random          # 导入 random 模块

print(math.sqrt(16))  # sqrt函数
print(math.pi)        # pi常量

print(random.randint(1, 10))                         # 随机1~10整数
print(random.choice(["apple", "banana", "cherry"]))  # 列表随机

from math import sqrt
print(sqrt(25))

print(math.floor(3.8))  # 向下取整
print(math.ceil(3.2))   # 向上取整
print(math.sqrt(81))
print(random.randint(1, 100))
print(random.choice(["redstone", "piston", "obsidian"]))
from math import floor
print(floor(9.9))