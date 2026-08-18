# dict_basics.py — 字典:键值对,用「名字」查东西
students = {"name": "URNR", "age": 20, "major": "CS"}
print(students["name"])
print(students["age"])

students["age"] = 21          # 改:key 已存在 → 修改
students["city"] = "Beijing"  # 加:key 不存在 → 新增
print(students)
print("name" in students)  # True
print("height" in students)  # False
print(len(students))  

for k, v in students.items():  # 遍历字典
    print(f"{k}: {v}")

dick = {"name": "LWS", "age": 19, "major": "robotics"}
print(dick["name"])
dick["sex"] = "male"
dick["age"] = 20
print("age" in dick)
for a, b in dick.items():
    print(f"{a}: {b}")
#test
