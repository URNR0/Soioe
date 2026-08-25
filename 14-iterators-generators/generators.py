it = iter("hello")
while True:
    try:
        n = next(it)       # 游标前进一格,返回当前元素
    except StopIteration:
        break              
    print(n)

def my_range(start, stop):
    while start <= stop:
        yield start
        start += 1
for x in my_range(1, 5):
    print(x)

def fib(n):
    if n <= 0:
        return
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fib(10):
    print(num, end=" ")

print(sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0))
print(sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0]))  # 内存占用大

def even_numbers():
    x = 0
    while True:
        yield x
        x += 2

gen = even_numbers()
print(next(gen))  # 0
print(next(gen))  # 2
print(next(gen))  # 4
print(next(gen))  # 6
print(next(gen))  # 8