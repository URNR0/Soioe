# oop_basics.py — 类与对象:数据 + 行为打包在一起
import math

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"大家好，我是 {self.name}，今年 {self.age} 岁。")

s1 = Student("URNR", 20)
s2 = Student("Soioe", 22)
s1.introduce()     # 调用方法(不用写 self,自动传)
s2.introduce()

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def describe(self):
        print(f"这是一辆 {self.color} 的 {self.brand}。")

c1 = Car("Toyota", "红色")
c2 = Car("Honda", "蓝色")
c1.describe()
c2.describe()

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

circle1 = Circle(5)
print(circle1.area())