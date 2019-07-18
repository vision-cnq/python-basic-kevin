"""
    函数
        声明函数：
            def 函数名() :
                代码块...

"""

# 定义一个函数
def fn() :
    print('这是我的第一个函数')
    print('hello')
    print('今天天气不错')

# fn是函数对象，fn()调用函数
# print是函数对象，print()调用函数
fn()
print(type(fn))
print(type(print))

# 定义一个函数，可以用来求任意两个数的和
def sum() :
    a = 123
    b = 456
    print(a+b)

# 调用函数
sum()

# 定义函数时指定形参
def fn2(a,b) :
    print(a,"+",b,"=",a+b)

# 调用函数时，来传递实参
fn2(50,20)
