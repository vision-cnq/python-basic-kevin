"""
    返回值
        返回值就是函数执行以后返回的结果
        可以通过return来指定函数的返回值
        可以之间使用函数的返回值，也可以通过一个变量来接收函数的返回值
        函数中，return后的代码都不会执行，return一旦执行函数自动结束


"""

def sum(*nums) :
    # 定义一个变量，保存结果
    result = 0
    # 遍历数组，并将元组中的数进行累加
    for n in nums :
        result += n
    print(result)

sum(12,45,749,45)

# return 后边跟什么值，函数就会返回什么值
# return 后边可以跟任意的对象，返回值甚至可以是一个函数
def fn() :
    def fn2():
        print('hello')
    return fn2()    # 返回值可以是一个函数

r = fn()
print('fn() = ',fn())
print('r = ',r)

# 如果仅仅写一个return或者不写return，则相当于return None
def fn2():
    a = 10
    return
print('fn2() = ',fn2())

# 函数中，return后的代码都不会执行，return一旦执行函数自动结束
def fn3():
    print('hello')
    return
    print('abc')
r = fn3()
print(r)

def fn4():
    for i in range(5):
        if i == 3:
            # break 用来退出当前循环
            # continue用来跳过当次循环
            return  # return 用来结束函数
        print(i)
    print('循环执行完毕')
fn4()

def sum(*nums) :
    # 定义一个变量，来保存结果
    result = 0
    # 遍历元组，并将元组中的数进行累加
    for n in nums :
        result += n
    return result

r = sum(123,456,78)
print(r)

def fn5():
    return 10

# fn5和fn5()的区别
print(fn5) # fn5是函数对象，打印fn5实际是在打印函数对象
print(fn5()) # fn5()是在调用函数，打印fn5()实际上是在打印fn5()函数的返回值10
