"""
    类型转换：4个函数int() float() str() bool()
        int()可以将对象转换为整型
        float()可以将对象转换成浮点型
        str()可以将对象转成字符串
        bool()可以将对象转换成布尔值，任何对象都可以转换成布尔值
    规则：
        布尔值：True -> 1, False -> 0
        浮点数：直接取整，省略小数点后的内容
        字符串：合法的整数字符串直接转换成对应的数字
"""
a = 123

a = False
a = int(a)

a = '123'
a = int(a)

a = 11.6
a = int(a)

a = '11.5'
# a = int(a)

a = None
# a = int(a)

a = 1
a = float(a)

a = False
a = float(a)

a = 123
a = str(a)

a = None
a = bool(a)

print('a =',a)
print('a的类型是',type(a))