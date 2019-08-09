'''
    关闭文件
        调用close()方法来关闭文件
            例如：file_obj.close()

    读取文件中的内容
        read()：用来读取文件中的内容，它会将内容全部保存为一个字符串返回
            例如：content = file_obj.read()

    with ... as 语句
        with open(file name) as file_obj:
            print(file_obj.read())
        在这个with语句中可以直接使用file_obj来做文件操作
        此时这个文件只能在with中使用，一旦with结束则文件会自动close

'''

# 文件名
file_name = 'demo.txt'

# 打开文件
file_obj = open(file_name)

# 当我们获取了文件对象以后，所有的对文件的操作都应该通过对象来进行
content = file_obj.read()
print(content)

file_name = 'hello'

try:
    with open(file_name) as file_obj:
        print(file_obj.read())
except FileNotFoundError:
    print(f'{file_name} 文件不存在...')