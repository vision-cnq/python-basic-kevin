'''
    特殊方法，也称为魔术方法
    特殊方法都是使用__开头和结尾的
    特殊方法一般不需要我们手动调用，需要在一些特殊情况下自动执行

         object.__add__(self, other)
         object.__sub__(self, other)
         object.__mul__(self, other)
         object.__matmul__(self, other)
         object.__truediv__(self, other)
         object.__floordiv__(self, other)
         object.__mod__(self, other)
         object.__divmod__(self, other)
         object.__pow__(self, other[, modulo])
         object.__lshift__(self, other)
         object.__rshift__(self, other)
         object.__and__(self, other)
         object.__xor__(self, other)
         object.__or__(self, other)

         object.__lt__(self, other) 小于 <
         object.__le__(self, other) 小于等于 <=
         object.__eq__(self, other) 等于 ==
         object.__ne__(self, other) 不等于 !=
         object.__gt__(self, other) 大于 >
         object.__ge__(self, other) 大于等于 >=

         __len__()获取对象的长度
         __str__()可以用来指定对象转换为字符串的结果(print函数)
         __repr__()指定对象在交互模式中输出的效果
        __bool__(self)可以通过bool来指定对象转换为布尔值的情况
        __gt__会在对象做大于比较的时候调用，该方法的返回值将会作为比较的结果


'''
# 定义一个Person类
class Person(object):
    """人类"""
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # __str__()这个特殊方法会在尝试将对象转换成字符串的时候调用
    # 作用：可以用来指定对象转换为字符串的结果(print函数)
    def __str__(self):
        return 'Person [name = %s , age = %d]' %(self.name,self.age)

    # __repr__()这个特殊方法会在当前对象使用repr()函数时调用
    # 作用：指定对象在交互模式中输出的效果
    def __repr__(self):
        return 'Hello'

    # object.__bool__(self)
    # 可以通过bool来指定对象转换为布尔值的情况
    def __bool__(self):
        return self.age > 17

    # __gt__会在对象做大于比较的时候调用，该方法的返回值将会作为比较的结果
    # 他需要两个参数，一个self表示当前对象，other表示和当前对象比较的对象
    # self > other
    def __gt__(self, other):
        return self.age > other.age

# 创建两个Person类的实例
p1 = Person('KEVIN', 23)
p2 = Person('COCO', 20)

# 打印p1，当我们打印一个对象时，实际上打印的是对象的特殊方法__str__的返回值
print(p1)
print(p2)

print(repr(p1))

t = 1,2,3
print(t)

print(p1>p2)
print(p2 > p1)

print(bool(p1))