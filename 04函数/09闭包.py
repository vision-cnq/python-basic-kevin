"""
    闭包
        将函数作为返回值返回，也是一种高阶函数，成为闭包
        通过闭包可以创建一些只有当前函数能访问的变量，可以将一些私有的数据藏到闭包中
        通俗解释：
            在一个外部函数中定义了一个内部函数，内部函数里运用了外部函数的临时变量，并且外部函数的返回值
            是内部函数的引用，这样就形成了闭包。
    形成闭包的要件
        1.函数嵌套
        2.将内部函数作为返回值返回
        3.内部函数必须要使用到外部函数的变量

"""

def fn():
    a = 10
    # 函数内部再定义一个函数
    def inner():
        print('我是fn2: ',a)
    # 将内部函数inner作为返回值返回
    return inner

# r是一个函数，是调用fn()后返回的函数，这个函数是在fn()内部定义，并不是全局函数，所以这个函数总是能访问到fn()函数内的变量
r = fn()
print(r())

# 求多个数的平均值
nums = [50,30,20,10,77]

# sum()用来求一个列表中所有元素的和
print(sum(nums) / len(nums))
print('sum(nums) = ',sum(nums))
print('len(nums) = ',len(nums))

# 闭包，将函数作为返回值
def make_averager():
    # 创建一个列表，用来保存数值
    nums = []
    # 创建一个内部函数，用来计算平均值
    def averager(n):
        # 将n添加到列表中
        nums.append(n)  # 内部函数中用到了外部函数的临时变量
        # 求平均值
        print('sum(nums) = ',sum(nums) ,'len(nums) = ', len(nums))
        return sum(nums) / len(nums)
    # 外部函数的返回值是内部函数的引用
    return averager

averager = make_averager()

print(averager(10))
print(averager(20))
print(averager(30))






