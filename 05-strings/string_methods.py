# string_methods.py — 字符串方法:处理文本的瑞士军刀
s = "  Hello, Python World  "
print(s.strip())
print(s.upper())
print(s.lower())
print(s.replace("Hello", "URNR"))

print(len(s))
words = s.split(",")
print(words)

print(s)  # 字符串不变

sentence = "  Python is fun, Python is powerful  "
new_sentence = sentence.strip()
print(new_sentence.upper())
print(new_sentence.replace("Python", "C"))
print(new_sentence.find("fun"))
new_words = new_sentence.split(" ")
print(new_words)
for word in new_words:
    print(word)
print(" ".join(new_words))
