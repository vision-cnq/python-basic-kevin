"""
    高阶函数
        接收函数作为参数，或者将函数作为返回值的函数是高阶函数
        当我们使用一个函数作为参数时，实际上是将指定的代码传递进目标函数

    filter()
        filter()可以从序列中过滤出符合条件的元素，保存到一个新的序列中
        参数：
            1.函数，根据该函数来过滤序列（可迭代的结构）
            2.需要过滤的序列（可迭代的结构）
        返回值：
            过滤后的新序列（可迭代的结构）

    匿名函数lambda函数表达式（语法糖）
        lambda函数表达式专门用来创建一些简单的函数，它是函数创建的又一种方式
        语法：lambda
        参数列表：返回值
        匿名函数一般都是作为参数使用，其它地方一般不会使用

    map()
        map()函数可以对可跌倒对象中的所有元素做指定的操作，然后将其添加到一个新的对象中返回

    sort()
        该方法用来对列表中的元素进行排序
        sort()方法默认是直接比较列表中的元素的大小
        在sort()可以接收一个关键字参数，key
            key需要一个函数作为参数，当设置了函数作为参数

    sorted()
        这个函数和sort()的用法基本一致，但是sorted()可以对任意序列进行排序
        并且使用的sorted()排序不会影响原来的对象，而是返回一个新对象

"""

# 创建一个列表
a = [1,2,3,4,5,6,7,8,9,10]

# 定义一个函数
# 将指定列表中的所有的偶数，保存到一个新的列表中返回

# 定义一个函数，用来检查一个任意的数字是否是偶数
def fn2(i):
    if i % 2 == 0:
        return True
    return False

# 这个函数用来检查指定的数字是否大于5
def fn3(i):
    if  i > 5:
        return True
    return False

def fn(func,lst):
    """
        fn()函数可以指定列表中的所有偶数获取出来，并保存到一个新列表中返回
    :param func: 作为参数传入的函数
    :param lst: 要进行筛选的列表
    :return:
    """
    # 创建一个新列表
    new_list = []
    # 对列表进行筛选
    for n in lst:
        # 判断n的奇偶
        if func(n):
            new_list.append(n)
    # 返回新列表
    return new_list

# 被传入的函数，判断奇偶
def fn4(i):
    return i % 3 == 0

"""
    fn4是作为参数传递进filter函数中
        而fn4实际上只有一个作用，就是作为filter()的参数
        filter()调用完毕后，fn4就已经没用了
"""
print(fn(fn4,a))

def fn5(a,b):
    return a + b

# (lambda a,b : a+b)(10,20)
# 也可以将匿名函数赋值给一个变量，一般不会这么做
fn6 = lambda a,b : a+b
print(fn6(10,30))

# filter()可以从序列中过滤出符合条件的元素，保存到一个新的序列中
r = filter(lambda i : i > 5, a)
print(list(r))


# map()函数可以对可跌倒对象中的所有元素做指定的操作，然后将其添加到一个新的对象中返回
m = map(lambda i : i ** 2, a)
print(list(m))

# sort()该方法用来对列表中的元素进行排序,每次都会以列表中的一个元素作为参数来调用函数，并使用函数的返回值比较元素的大小
s = ['bb','aaaa','c','ddddddddd','fff']
s.sort(key=len)
print(s)

s = [2,5,'1',3,'6','4']
s.sort(key=int)
print(s)

# sorted()可以对任意的序列进行排序，且不会影响之前的对象，而是返回一个新的对象
s = [2,5,'1',4,'6',3]
print('排序前: ',s)
print(sorted(s,key=int))    
print('排序后: ',s)    # 并没有影响之前的对象
