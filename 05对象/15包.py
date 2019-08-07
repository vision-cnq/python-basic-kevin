'''
    包 Package
        包也是一个模块
        语法：form 包名 import 模块1,模块2
        例如：form hello import a,b        # 引入例如两个模块
    当我们模块中代码过多时，或者一个模块需要被分解为多个模块时，这时就需要用到包
    普通的模块就是一个py文件，而包是一个文件夹
    包中必须要有一个__init__.py的文件，这个文件中可以包含有包中的主要内容

'''
from hello import a,b
print(a.c)
print(b.d)







