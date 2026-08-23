# oop_advanced.py — 继承、覆盖、__str__
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows!")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()
cat.speak()

# __str__:让 print(对象) 显示自定义内容
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student({self.name}, {self.age})"

s = Student("URNR", 19)
print(s)           # Student(URNR, 19) —— 不再是 <...object...>

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def move(self):
        print(f"{self.brand} is moving.")

class Car(Vehicle):
    def move(self):
        print(f"{self.brand} is driving on the road.")
    def __str__(self):
        return f"Car(brand = {self.brand})"
class Bike(Vehicle):
    def move(self):
        print(f"{self.brand} is riding on the path.")

car = Car("Toyota")
bike = Bike("Yamaha")

car.move()
bike.move()
print(car)  # Car(brand = Toyota)