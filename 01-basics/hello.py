# hello.py — Lesson 1 第一个 Python 程序
# 对照 C 来记:没有分号 ;、没有大括号 {}、变量不声明类型
# 1. 用 print 输出自我介绍 (print ≈ C 的 printf,会自动换行)
print("Hello,World!")
print("我是URNR,一个人类")
# 2. 定义 4 个基本类型的变量: int / float / str / bool
age = 19           # int    整数(注意:没有溢出,想多大都行)
base = 1.75        # float  浮点数
name = "URNR"      # str    字符串(单引号 ' ' 或双引号 " " 都可以)
is_student = True  # bool   布尔值,注意首字母大写!
print(age)
print(base)
print(name)
print(is_student)
# 用 type() 查看每个变量的类型(现在变量是什么类型)
print(type(age))
print(type(base))
print(type(name))
print(type(is_student))
# 3. 用 f-string 把变量拼进一句话(f 开头,{ } 里直接放变量名)
print(f"名字{name}，{age}，{base}，我是一名学生吗？{is_student}")
# 4. 一个简单的 if 判断,演示 bool 的用法(预告:下一课专门讲)
#    对比 C:没有 if (...) 的括号,没有花括号,用「冒号 + 缩进」代替
if is_student:
    print("是的，我是一名学生")