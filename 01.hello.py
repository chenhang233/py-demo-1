
from sys import path


print("hello world")
# 单行注释

"""
多行注释
"""

if True:
    print("true")
else :
    print("false")
print("path",path)

list = ["列表","22",34]

list[2] = 55

print(list)


inputRef = input("请输入字符")

reverse = inputRef.split(" ")[-1::-1]

print(" ".join(reverse))

receive = "==##"
print(receive.startswith("==##"),"fffff")

