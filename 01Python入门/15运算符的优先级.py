"""
    运算符的优先级
        和数学一样，python运算也拥有优先级，比如：先乘除后加减。
        运算符的优先级可以根据优先级的表格来查询
            在表格中位置越靠下的运算符优先级越高，优先级越高的越优先计算
            如果优先级一样，则自左向右计算
        如果开发时遇到优先级不清楚的，则可以通过小括号来改变运算顺序

"""

a = 1 + 2 * 3
print(a)

# and 与 or优先级一样高，优先运算顺序在前的
a = 1 or 2 and 3    # 1
a = 2 and 3 or 1    # 3
print(a)



