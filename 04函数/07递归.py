"""
    尝试求10的阶乘(10!)
        1! = 1
        2! = 1*2 = 2
        3! = 1*2*3 = 6
        4! = 1*2*3*4 = 24

    递归式的函数
        递归式函数，在函数中自己调用自己
            递归是解决问题的一种方式，和循环很像
            整体思想是，将一个大问题分解为一个个小问题，直到问题无法分解时再解决问题。
        递归式函数的两个要件
            1.基线条件
                问题可以被分解为最小问题，当满足基线条件时，递归不再执行
            2.递归条件
                将问题继续分解的条件
        递归与循环类似，基本是可以互相替代的
        循环编写起来比较容易，阅读起来稍难，递归编写起来难，但是方便阅读

    无穷递归
        如果这个函数被调用，程序的内存会溢出，类似死循环
        def fn():
            fn()
        fn()

"""

# 求10的阶乘(10!)
n = 10
for i in range(1,10):
    n *= i
print(n)

# 创建一个函数，可以用来求任意数的阶乘
def factorial(n):
    """
        该函数用来求任意数的阶乘
    :param n: 要求阶乘的数字
    :return:
    """
    # 创建一个变量，来保存结果
    result = n
    for i in range(1,n):
        result *= i
    return result

# 求10的阶乘
print(factorial(10))

# 创建一个递归式函数，可以用来求任意数的阶乘
def factorial(n):
    """
        该函数用来求任意数的阶乘
    :param n: 要求阶乘的数字
    :return:
    """
    # 基线条件，判断n是否为1，如果为1则此时不能再继续递归
    if n == 1:
        # 1的阶乘就是1，直接返回1
        return 1
    # 递归条件
    return n * factorial(n-1)

print(factorial(10))

"""
    创建一个函数power来为任意数字做幂运算 n ** i
        10 ** 5 = 10 * 10 ** 4
        10 ** 4 = 10 * 10 ** 3
        ...
        10 ** 1 = 10
"""
# 创建一个递归式函数，可以为任意数字做幂运算
def power(n,i):
    """
        power()用来为任意的数字做幂运算
    :param n: 要做幂运算的数字
    :param i: 做幂运算的次数
    :return:
    """
    # 基线条件
    if i == 1:
        # 求1次幂
        return n
    # 递归条件
    return n * power(n,i-1)

print(power(8,6))


"""
    创建一个函数，用来检查一个任意的字符串是否是回文字符串，如果是返回True，否则返回False
        回文字符串，字符串从前往后念和从后往前念是一样的
            如果一致，则看剩余的部分是否是回文字符串
               检查 abcdefgfedcba 是不是回文
               检查 bcdefgfedcb 是不是回文
               检查 cdefgfedc 是不是回文
               检查 defgfed 是不是回文
               检查 efgfe 是不是回文
               检查 fgf 是不是回文
               检查 g 是不是回文
"""

def hui_wen(s):
    """
        该函数用来检查指定的字符串是否回文字符串，如果是返回True，否则返回False
    :param s:就是要检查的字符串
    :return:
    """
    # 基线条件
    if len(s) < 2:
        # 字符串的长度小于2，则字符串一定是回文
        return True
    elif s[0] != s[-1]:
        # 第一个字符和最后一个字符不相等，不是回文字符串
        return False
    # 递归条件
    return hui_wen(s[1:-1])

print(hui_wen('abcdefgfedcba'))

