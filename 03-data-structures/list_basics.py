# list_basics.py 手敲理解每一个基础操作
scores = [88, 92, 75, 60] # 列表用 [ ] ,逗号隔开
print(scores[0])
print(scores[-1])         # 最后一个元素:60(负数索引,从右边数,C 没有这个!)
print(len(scores))        # 长度:4(len 看这个容器有多大)
scores.append(100)        # 末尾加一个,列表自动变长(C 的数组做不到)
print(scores)

for s in scores:
    print(s)

lists = ["games", "pc", "books"]
print(lists[0])
print(lists[-1])
lists.append("keyboard")
print(lists)
for num, stuff in enumerate(lists, start = 1):
    print(f"{num}:{stuff}")
print(len(lists))