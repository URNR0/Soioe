# 1. 用列表推导式生成 0~9 的平方列表。
# 2. 用列表推导式,从 ["cat", "elephant", "dog", "giraffe"] 里筛出长度 > 3 的字符串。
# 3. 用列表推导式,把 ["apple", "banana", "cherry"] 全部转成大写。
# 4. 用字典推导式:给定 names = ["Alice", "Bob", "Cara"],生成 {名字: 名字长度}。
# 5. 用集合推导式:从字符串 "hello world" 里取出所有出现过的字母(去重,空格不算)。
# 6. 挑战(嵌套推导式):用一行生成 3×3 乘法表(列表的列表): [[1,2,3], [2,4,6], [3,6,9]]
# —— 提示:想清楚谁是外层(每一行)、谁是内层(每行里的每个数)。



print([x * x for x in range(10)])
print([x for x in ["cat", "elephant", "dog", "giraffe"] if len(x) > 3])
print([x.upper() for x in ["apple", "banana", "cherry"]])
print({name: len(name) for name in ["Alice", "Bob", "Cara"]})
print({char for char in "hello world" if not char.isspace()})
print([[x * y for y in range(1, 4)] for x in range(1, 4)])
