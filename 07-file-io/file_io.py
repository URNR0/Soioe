# file_io.py — 文件读写:让程序「记住」数据
# 1. 写文件(w 模式:覆盖写)
with open("note.txt", "w") as f:
    f.write("第一行\n")
    f.write("第二行\n")

# 2. 读文件(r 模式:只读)
with open("note.txt", "r") as f:
    content = f.read()  #读取整个文件内容
    print(content)

# 3. readlines:读成列表,每行一个元素(注意带着 \n)
with open("note.txt", "r") as f:
    lines = f.readlines()
    print(lines)

with open("about_me.txt", "w") as f:
    f.write("姓名: 张三\n")
    f.write("年龄: 25\n")
    f.write("爱好: piano\n")

with open("about_me.txt", "r") as f:
    content1 = f.read()
    print(content1)

with open("about_me.txt", "r") as f:
    lines1 = f.readlines()
    lines1 = [line.strip() for line in lines1]  # 去掉每行的换行符
    for line in lines1:
        print(line)

with open("about_me.txt", "a") as f:
    f.write("补充: 软件工程师\n")

with open("about_me.txt", "r") as f:
    content1 = f.read()
    print(content1)

