"""
    通过类型检查，可以检查值、变量的类型
        type()用来检查值的类型
        该函数会将检查的结果作为返回值返回，可以通过变量来接收函数的返回值
"""
a = 123
c = type('123')
c = type(a)
print(c)

print(type(1))
print(type(1.5))
print(type(True))
print(type('hello'))
print(type(None))