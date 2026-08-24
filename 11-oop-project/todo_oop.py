# todo_oop.py — OOP 版待办清单

class Task:
    def __init__(self, description):
        self.description = description
        self.done = False
    
    def __str__(self):
        mark = "✓" if self.done else " "
        return f"[{mark}] {self.description}"
    
    def mark_done(self):
        self.done = True

class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"已添加：{description}")

    def show(self):
        if not self.tasks:
            print("清单是空的")
        else:
            for i, t in enumerate(self.tasks, start=1):
                print(f"{i}. {t}")
    
    def remove(self, index):
        if 1 <= index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            print(f"已删除：{removed.description}")
        else:
            print("编号无效！")
    
    def save(self):
        with open("tasks.txt", "w") as f:
            for t in self.tasks:
                flag = "1" if t.done else "0"
                f.write(f"{t.description}|{flag}\n")
        print(f"已保存{len(self.tasks)}个任务")
    
    def load(self):
        try:
            with open("tasks.txt", "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:                       # 跳过空行
                        continue
                    desc, flag = line.split("|")       # 按 | 拆成两部分(解包!)
                    task = Task(desc)
                    if flag == "1":                    # 字符串比较
                        task.mark_done()
                    self.tasks.append(task)
            print(f"已加载 {len(self.tasks)} 个任务")
        except FileNotFoundError:
            print("还未保存过~从空清单开始")
    
    def mark_done(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1].mark_done()
            print(f"已完成: {self.tasks[index - 1].description}")
        else:
            print("编号无效")
        
todo = TodoList()
todo.load()

while True:
    print("\n1. 查看  2. 添加  3.标记为完成  4. 删除  5. 保存  6. 退出")
    choice = input("请选择：")
    if choice == "1":
        todo.show()
    elif choice == "2":
        desc = input("请输入任务：")
        todo.add(desc)
    elif choice == "3":
        todo.show()
        num = int(input("要标记第几个？"))
        todo.mark_done(num)
    elif choice == "4":
        todo.show()
        num = int(input("要删除第几个？"))
        todo.remove(num)
    elif choice == "5":
        todo.save()
    elif choice == "6":
        print("再见~")
        break

