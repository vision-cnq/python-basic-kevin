"""
    逻辑运算符
        主要做一些逻辑判断
        not 逻辑非
            对于布尔值，非运算会对其进行取反操作，True变False，False变True
            对于非布尔值，非运算会先将其转换为布尔值，然后再取反
        and 逻辑与
            只有在符号两侧的值都为True时，才会返回True，只要有一个False就返回False
        or 逻辑或
             or 可以对符号两侧的值进行或运算。或运算两个值中只要有一个True，就会返回True
"""


a = True
a = not a # 对a进行非运算

a = 1
a = ''
a = not a
# print('a =',a)

result = True and True # True
result = True and False # False
result = False and True # False
result = False and False # False

result = True or True # True
result = True or False # True
result = False or True # True
result = False or False # False


# True and True
result = 1 and 2 # 2
# True and False
result = 1 and 0 # 0
# False and True
result = 0 and 1 # 0
# False and False
result = 0 and None # 0

# True or True
result = 1 or 2 # 1
# True or False
result = 1 or 0 # 1
# False or True
result = 0 or 1 # 1
# False or False
result = 0 or None # None

# 逻辑运算符可以连着使用
result = 1 < 2 < 3  # 相当于1 < 2 and 2 < 3
result = 10 < 20 > 15

print(result)
