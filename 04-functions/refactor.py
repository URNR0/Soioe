def fizzbuzz(n):
    # 你填:判断 n,返回 "FizzBuzz" / "Fizz" / "Buzz" / 数字本身
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

def print_row(i):
    for j in range(1, i + 1):
        print(f"{j}x{i}={i*j}", end="  ")
    print()  

for i in range(1, 16):
    print(fizzbuzz(i))

print()          # 空一行,分隔两部分输出

for i in range(1, 10):
    print_row(i)