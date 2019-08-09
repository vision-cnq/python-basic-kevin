'''
    readline()
        该方法用来读取一行内容
            例如：print(file_obj.readline())

    readlines()
        该方法用来一行一行的读取内容，会一次性读取完，将内容封装到列表返回

'''

import pprint
import os

file_name = 'demo.txt'

with open(file_name, encoding='utf-8') as file_obj:
    # 读取一行数据
    print(file_obj.readline(),end='')   # 加上end=''，结束时便不会换行
    print(file_obj.readline())          # 结束时会换行
    print(file_obj.readline())

    r = file_obj.readlines()
    pprint.pprint(r[0])
    pprint.pprint(r[1])

    for t in r:
        print(t)
        # print(t, end='')
