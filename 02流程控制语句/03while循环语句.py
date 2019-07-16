"""
    循环语句
        while 语句
            语法：
                while 条件表达式 :
                    代码块
                else :
                    代码块
            执行流程：
                while语句在执行时，会先对while后的条件表达式进行求值判断
                    如果判断结果为True，则执行循环体（代码块）
                    循环体执行完毕，继续对条件表达式进行求值判断，以此类推
                如果判断结果为False，则循环终止，如果循环有对应的else，则执行else后的代码块

        死循环：
            while True :
                print("hello world !")

            循环的三个要件（表达式）
                初始化表达式，通过初始化表达式初始化一个变量
                i = 0

        条件表达式
            while i < 10 :
                print(i)
                i += 1
            条件表达式用来设置循环执行的条件
"""

# 创建一个执行十次的循环
i = 0
while i < 10 :
    # print(i)
    i += 1
else :
    print("else的代码")



# 求100以内的所有奇数之和
i = 0
result = 0  # 保存奇数之和
while i < 100 :
    i += 1
    # 判断是否为奇数
    if i % 2 != 0 :
        result += i
print("100内的奇数之和: ",result)



# 求100以内所有7的倍数之和，以及个数
i = 7
result = 0 # 保存结果
count =0 # 计数器
while i < 100 :
    count += 1
    result += i
    i += 7
print("100内7的倍数之和为: ",i,"数量为: ",count)



# 水仙花数是指一个n位数(n >= 3)，它的每个位上的数字n的次幂之和等于它本身（例如：1**3 + 5**3 + 3**3 = 153）

# 求1000以内的所有水仙花数
i = 100
while i < 1000 :
    a = i // 100    # 求i的百位数
    b = (i-a*100) // 100    # 求i的十位数
    c = i % 10      # 求i的个位数
    # 判断i是否是水仙花数
    if a**3 + b**3 + c**3 == i :
        print(i)
    i += 1



# 获取用户输入的任意数， 判断其是否是质数
num = int(input('输入一位任意大于1的整数: '))

# 判断num是否是质数，只能被1和它自身整除的数就是质数
# 获取到所有的可能整除num的整数

i = 2
# 创建一个变量，用于记录num是否是质数，默认认为num是质数
flag = True
while i < num :
    # 判断num能否被i整除
    # 但如果num能被i整除，则说明num一定不是质数
    if num % i == 0 :
        # 一旦进入判断，则证明num不是质数，则需要将flag修改成false
        flag = False
    i += 1

if flag :
    print(num, "是质数")
else :
    print(num,"不是质数")