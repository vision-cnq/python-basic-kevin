'''
    调用open()来打开一个文件，可以将文件分成两种类型
        1.纯文本文件（使用utf-8f等编码编写的文本文件）
        2.二进制文件（图片，map3，ppt等这些文件）

        open()打开文件时，默认是以文本文件的形式打开的，但是open()默认编码为None，所以在处理文本文件时，必须要指定文件的编码

    通过 read() 来读取文件中的内容
        如果直接调用read()它会将文本文件的所有内容全部都读取出来，
        如果要读取的文件较大的话，会一次性将文件的内容加载到内存中，容易导致内存泄漏，
        所以对于较大的文件，不要直接调用read()

    read()可以接收一个size作为参数，该参数用来指定要读取的字符的数量
        默认值为-1，它会读取文件中的所有字符
        可以为size指定一个值，这样read()会读取指定数量的字符，
        每一次读取都是从上次读取到位置开始读取的
        如果字符的数量小于size，则会读取剩余所有的
        如果已经读取到了文件的最后了，则会返回''空串
'''

file_name = 'demo2.txt'

try:
    # 操作文件
    with open(file_name,encoding='utf-8') as file_obj:
        # help(file_obj.read())
        # 指定读取的长度
        content = file_obj.read(6)
        print(content)
except FileNotFoundError:
    print(f'{file_name} 这个文件不存在...')


# 读取大文件的方式
file_name = 'demo.txt'

try:
    # 操作文件
    with open(file_name,encoding='utf-8') as file_obj:
        # 定义一个变量，来保存文件的内容
        file_content = ''
        # 定义一个变量，来指定每次读取的大小
        chunk = 100
        # 创建一个循环来读取文件内容
        while True:
            # 读取chunk大小的内容
            content = file_obj.read(chunk)
            # 检查是否读取到了内容
            if not content:
                # 已经没有内容了，代表已经读取完毕，退出循环
                break

            # 输出内容
            file_content += content
except FileNotFoundError:
    print(f'{file_name} 文件不存在')

print(file_content)