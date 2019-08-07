'''
    模块（module）
        模块化，模块化指将一个完整的程序分解为一个一个小的模块
        通过将模块组合，来搭建出一个完整的程序
        不采用模块化，统一将所有的代码编写到一个文件
        采用模块化，将程序分别编写到多个文件中
            模块化的优点：
                1.方便开发
                2.方便维护
                3.模块可以复用
        在python中，一个py文件就是一个模块，实际上就是创建一个模块
        注意：模块名要符号标识符的规范。

        在一个模块中引入外部模块
            1.import 模块名    （模块名，就是python文件的名字，但不需要py后缀）
            2.import 模块名 as 模块别名
                可以引入同一个模块多次，但是一般情况下，import语句都统一写在文件的开头
                在每一个模块内部都有一个__name__属性，一个程序中只会有一个主模块
                主模块就是我们直接通过python执行的模块
            import m
            import m as test

        也可以只引入模块中的部分内容
            语法 from 模块名 import 变量,变量....
            from m import Person

        也可以为引入的变量使用别名
            语法：from 模块名 import 变量 as 别名
            from m import test2 as new_test2

'''
# import m
# # 访问模块中的变量：模块名.变量名
# print(m.a, m.b)
# m.test2()
#
# p = m.Person()
# print(p.name)

def test2():
    print('这是主模块中的test2')

# 引入模块的部分内容
from m import Person
p1 = Person()
print(p1.name)

# 引入的变量使用别名
from m import test2 as new_test2
test2()
new_test2()

from m import *
print(b)
# print(_c)     # _开头的属性无法引入



