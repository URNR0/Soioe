my_functions = [len, abs]

print(my_functions)  
# [<built-in function len>, <built-in function abs>]

# 类型
print(type(my_functions[0]))  
print(type(my_functions[1]))  

# 调用（len）
print(my_functions[0]("Hello"))    
print(my_functions[0]([1, 2, 3]))  

# 调用（abs）
print(my_functions[1](-5))         
print(my_functions[1](-3.14))      

def make_adder(n):
    """创建一个加法器，记住参数 n"""
    def add(x):
        return x + n
    return add

add5 = make_adder(5)      
print(add5(10))           

add10 = make_adder(10)    
print(add10(10))          
print(add5(20))    

def announce(func):
    def wrapper():
        print("------------")
        func()
        print("------------")
    return wrapper

def uppercase_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_result
def get_message():
    return "hello world"

@announce
def prt():
    print("hello world")


print(get_message())
print(prt())

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(5)
def hello():
    print("hi")

hello()   # 打印 5 次 hi