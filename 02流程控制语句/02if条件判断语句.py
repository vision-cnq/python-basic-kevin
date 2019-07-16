"""
    条件判断语句
        代码块：以缩进开始，知道代码恢复之前的缩进级别时结束。

    if 语句
        语法：
            if 条件表达式 :
                代码块
        执行的流程：if语句在执行时，会先对条件表达式进行求值判断，
            如果为True，则执行if后的语句
            如果为False，则不执行
        默认情况下，if语句只会控制紧随其后的那条语句，如果希望if可以控制多天语句

    if else 语句
        语法：
            if 条件表达式 :
                代码块
            else :
                代码块
        执行流程：if-else语句在执行时，先对if后的条件表达式进行求值判断
            如果为True，则执行if后的代码块
            如果为False，则执行else后的代码块

    if elif else 语句
        语法：
            if 表达式 :
                代码块
            elif 条件表达式:
                代码块
            elif 条件表达式:
                代码块
            else :
                代码块
        执行流程：if-elif-else语句在执行时，会自上向下依次对条件表达式进行求值判断
            如果表达式的结果为True，则执行当前代码块，然后语句结束
            如果表达式的结果为False，则继续向下判断，直到找到True为止
            如果所有的表达式都是False，则执行else后的代码块
            if-elif-else中只会有一个代码块会执行
"""

# if    语句
num = 28

if num >= 10 :
    print('xxx')

if True :
    print(123)
    print(456)
    print(789)

# 连续判断
if num > 10 or num < 20 :
 print('num比10大或者num比20小！')

if 10 < num < 20 :
 print('num比10大,num比20小！')


# if else   语句
age = 7
if age > 17 :
    print('已成年')
else :
    print('未成年')


# if elif else  语句
age = 50
if age >= 18 and age < 30 :
    print("成年人")
elif age >= 30 and age < 60:
    print("中年人")
elif age >= 60 :
    print("老年人")


height = 188
money = 1888
face = 888

if height >= 180 and money > 1000 and face > 500 :
    print("高富帅")
elif height >= 180 or money > 1000 or face > 500 :
    print("虽不是完美也能凑合")
else :
    print("矮丑穷")