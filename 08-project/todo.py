# todo.py — 待办清单(第一版:查看 + 添加 + 退出)
tasks = []                        # 用列表存任务

def show_task():
    if not tasks:
        print("当前没有任务。")
    else:
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

def add_task():
    task = input("请输入任务：")
    tasks.append(task)
    print(f"已添加：{task}")

def delete_task():
    if not tasks:                           # 清单是空的,没得删,提前 return
        print("没有要删除的任务")             # 先显示编号,让用户知道删哪个
        return
    show_task()
    num = int(input("要删除第几个任务？"))
    if 1 <= num <= len(tasks):
        removed = tasks.pop(num - 1)           # 删除任务
        print(f"已删除：{removed}")
    else:
        print("无效的编号")

def save_task():
    with open("tasks.txt", "w") as f:   # 用 07 课学的文件写入
        for t in tasks:
            f.write(t + "\n")           # 每个任务占一行
    print(f"已保存{len(tasks)}个任务到 tasks.txt")

def load_task():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                tasks.append(line.strip())  # 去掉换行符
        print(f"已加载{len(tasks)}个任务")
    except FileNotFoundError:
        print("还未保存过，从空清单开始")

load_task()
while True:
    print("\n1. 查看任务  2. 添加任务  3. 删除任务  4. 保存任务  5. 退出")
    choice = input("请选择：")
    if choice == "1":
        show_task()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        save_task()
    elif choice == "5":
        print("再见~")
        break

