"""
    for循环
        语法：
            for 变量 in 序列 :
                代码块
        for循环的代码块会执行多次，序列中有几个元素就会执行几次，
        每执行一次就会将序列中的一个元素赋值给变量，所以可以通过变量获取到列表中的元素

        语法：
            for 变量 in 序列 :
                代码块
            else :
                代码块
"""

# 创建列表
stus = ['红孩儿', '红孩儿', '白骨精', '牛魔王', '孙悟空', '唐僧', '二郎神']

for s in stus :
    print(s)

for s in stus :
    if s == '唐僧21' :
        print('是的,跳出')
        break
    print('循环的数据: ' + s)
else :
    print('没有循环数据')
print('循环结束了')


# 遍历数字序列，可以使用内置range()函数。它会生成数列
for i in range(5) :
    print(i)

# 变量-10到-100内的数据，间隔-30
for i in range(-10, -100, -30):
    print(i)
