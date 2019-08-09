'''
    使用open函数来打开一个文件
    参数：
        file 要打开的文件的名字（路径）
    返回值：
        返回一个对象，这个对象就代表了当前打开的文件
'''

# 创建一个变量，来保存文件的名字
# 如果目标文件和当前文件在同一级目录下，则直接使用文件名即可
file_name = 'dome.txt'

# 在windows系统使用路径时，可以使用/来代替\
# 或者可以使用 \\ 来代替 \
# 或者也可以使用原始字符串
file_name = 'hello\\demo.txt'
file_name = r'hello\demo.txt'

# 表示路径，使用..来返回一级目录
file_name = '../hello/demo.txt'

# 如果目标文件距离当前文件比较远，此时可以使用绝对路径
# 绝对路径应该从磁盘的根目录开始书写
file_name = r'C:\Users\caonanqing\Desktop\demo.txt'

# 打开对应的文件
file_obj = open(file_name)

print(file_obj)



