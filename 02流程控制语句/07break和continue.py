"""
    break
        break可以用来立即退出循环语句，包括else
    continue
        continue可以用来跳过当次的循环
    pass
        pass是用来在判断或循环语句中占位的
    break和continue都是只对离他最近的循环起作用

"""

# 创建一个5次的循环
i = 0
while i < 5 :
    if i == 3 :
        break   # 跳出循环语句
    print(i)
    i += 1
else :
    print("循环结束")


i = 0
while i < 5 :
    i += 1
    if i == 2 :
        continue    # 跳出当次循环
    print(i)
else :
    print("循环结束")

i = 0
if i < 5 :
    pass