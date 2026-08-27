class Manager:
    def __enter__(self):
        print("进入")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"退出被调用了！")
        print(f"exc_type: {exc_type}")
        print(f"exc_val: {exc_val}")
        print(f"exc_tb: {exc_tb}")
        print("退出")

with Manager():
    print("干活中…")
print("\n")

#with Manager():
#    raise ValueError("出错了！")

try:
    with Manager():
        print("干活中…")
        raise ValueError("出错了！")
except ValueError as e:
    print(f"捕获到异常: {e}")


class Resource:
    def __enter__(self):
        print("资源已获取")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("资源已释放")
        if exc_type:
            print(f"  异常: {exc_val}")

# 测试1：正常使用
print("=== 正常 ===")
with Resource():
    print("干活中…")

# 测试2：异常使用
print("\n=== 异常 ===")
try:
    with Resource():
        print("干活中…")
        raise ValueError("出错了！")
except ValueError:
    print("外部捕获异常")

from contextlib import contextmanager

@contextmanager         
def contextmanagers():
    try:
        print("资源已获取")
        yield  # 把控制权交给 with 块
    except Exception as e:
        print(f"  异常: {e}")
        raise  # 让异常继续传播
    finally:
        print("资源已释放")

print("正常：")
with contextmanagers():
    print("运行中")

print("异常：")
try:
    with contextmanagers():
        print("运行中")
        raise ValueError("出错了！")
except ValueError:
    print("外部异常")
