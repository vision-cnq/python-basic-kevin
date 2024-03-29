"""
    不定长参数
        在定义函数时，可以在形参前边加上一个*，这样这个这个形参将会获取所有的实参，它将所有的实参保存到一个元组中

        带星号的形参只能有一个
            带星号的参数，可以和其他参数配合使用

        可变参数不是必须写在最后，但是注意，带*的参数后的所有参数，必须以关键字参数的形式传递

        如果在形参的开头直接写个*，则要求我们的所有参数必须以关键字参数的形式传递
            *形参只能接收位置参数，而不能接收关键字参数
            **形参可以接收其他的关键字参数，会将这些参数统一保存到一个字典中，字典的key就是参数名，value就是参数的值
            **形参只能有一个，并且必须写在所有参数的最后

        传递实参时，也可以在序列类型的参数前添加星号，这样会自动将序列中的元素依次作为参数传递

"""

# 定义一个函数，可以求任意个数字的和
# *nums会接受所有位置实参，并将这些实参统一放到一个元组中（装包）
def sum(*nums) :
    # 定义一个变量，来保存结果
    result = 0
    # 遍历元组，并将元组中的数进行累加
    for n in nums :
        result += n
    print(result)

sum(123,4,56,789,856)

# 第一个参数给a，第二个参数给b，剩下的都保存到c的元组中
def fn2(a,b,*c) :
    print('a = ',a)
    print('b = ',b)
    print('c = ',c)

fn2(45,789,456,15,48,5,635,45)

# 第一个参数给a，剩下位置参数给b的元组，c必须使用关键字参数
def fn2(a,*b,c) :
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)

fn2(45,45,8,97,c=5)

# 所有位置的参数给a，b、c必须使用关键字参数
def fn2(*a,b,c) :
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)

fn2(45,45,8,b=97,c=5)

# 如果在形参的开头直接使用一个*，则要求我们的所有参数必须以关键字参数的形式传递
def fn2(*,a,b,c) :
    print('a = ',a)
    print('b = ',b)
    print('c = ',c)

fn2(a=12,b=54,c=23)

# **形参可以接收其他的关键字参数，它会将这些参数统一保存到一个字典中,**形参只能有一个，并且必须写在所有参数的最后
def fn3(b,c,**a) :
    print('a = ',a,type(a))
    print('b = ',b)
    print('c = ',c)

fn3(b=1,d=2,c=3,e=10,f=20)

# 参数的解包（拆包）
def fn4(a,b,c) :
    print('a = ',a)
    print('b = ',b)
    print('c = ',c)

# 创建一个元组
t = (10,20,30)

# 要求序列中元素的个数必须和形参的个数一致
fn4(*t)

# 创建一个字典
d = {'a':100,'b':200,'c':300}
# 通过 **来对一个字典进行解包操作
fn4(**d)

