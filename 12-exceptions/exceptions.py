# exceptions.py — 异常处理:让程序遇到错误时不崩溃

# 0. 没有处理时,错误直接中断程序
# print(10 / 0)   # 取消注释:ZeroDivisionError

# 1. try/except:捕获指定的异常
try:
    result = 10 / 0
except ZeroDivisionError:
    print("不能除以 0!")

# 2. 捕获多种异常,或用 Exception 兜底
try:
    num = int("abc")       # 字符串不能转整数
except ValueError:
    print("这串字符不是数字")

try:
    num = int("abc")
except (ValueError, TypeError):   # 同时捕获多个异常
    print("类型或值不对")

# 3. as e:拿到异常对象,查看具体信息※
try:
    x = [1, 2, 3]
    print(x[10])
except IndexError as e:
    print(f"越界了:{e}")

# 4. else:try 块没出错时才执行
try:
    result = 10 / 2
except ZeroDivisionError:
    print("除以 0 了")
else:
    print(f"成功,结果是 {result}")

# 5. finally:无论是否出错都执行(常用于清理资源)
try:
    f = open("不存在.txt", "r")
except FileNotFoundError:
    print("文件不存在")
finally:
    print("这行一定会执行")

# 6. raise:自己主动抛出异常
def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为 0")   # 主动抛错,提醒调用者
    return a / b

try:
    print(divide(10, 0))
except ValueError as e:
    print(f"出错:{e}")

# 7. 自定义异常:继承 Exception,给错误起个有意义的名字
class InvalidAgeError(Exception):
    """年龄不合法时抛出的异常"""

def set_age(age):
    if not (0 <= age <= 150):
        raise InvalidAgeError(f"年龄 {age} 不合理")
    print(f"年龄设置为 {age}")

try:
    set_age(-5)
except InvalidAgeError as e:
    print(f"捕获到自定义异常:{e}")

# ===== 练习 =====
# 1. 写一个 get_int() 函数:反复让用户输入,直到输入合法整数才返回
#    (提示:input() 拿到的永远是字符串,int() 失败会抛 ValueError)
#
# 2. 给之前 08/11 的待办清单加上异常处理:
#    用户输入菜单序号时,如果输入的不是数字,不要崩溃,而是提示重试

def get_int():
    while True:
        try:
            return int(input("请输入一个整数："))
        except ValueError:
            print("无效！请输入整数！")

while True:
    choice = input("\n请输入你的选择(1-5):").strip()
    if not choice:
        print("❌ 输入不能为空，请重新选择")
        continue
    try:
        choice_num = int(choice)
    except ValueError:
        print("❌ 输入无效！请输入数字 1-5")
        input("\n按 Enter 键继续...")
        continue
    if choice_num < 1 or choice_num > 5:
        print("❌ 无效选择！请输入 1-5 之间的数字")
        input("\n按 Enter 键继续...")
        continue
    print(f"你选择了{choice}")
    break

    