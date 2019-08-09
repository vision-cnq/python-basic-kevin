'''
    os.listdir()
        获取指定目录的目录结构
            需要一个路径作为参数，会获取到该路径下的目录结构，默认路径为当前目录
            该方法返回一个列表，目录中的每一个文件（夹）的名字都是列表中的一个元素
    os.getcwd()
        获取当前所在的目录
    os.chdir()
        切换当前所在的目录 作用相当于 cd
    os.mkdir()
        创建目录
    os.rmdir()
        删除目录
    os.remove()
        删除文件
    os.rename('旧名字','新名字')
        重命名文件，或移动文件
    os.rename('源文件','目标文件')
        移动文件



'''
import os
from pprint import pprint

# 获取当前目录的目录结构
r = os.listdir()

# 获取当前所在的目录
r = os.getcwd()

# 切换当前所在的目录
# os.chdir('c:/')
# r = os.getcwd()

# 创建目录
os.mkdir("aaa")

# 删除目录
os.rmdir("aaa")

open('aa.txt','w')
# 删除文件
os.remove('demo5.txt')

# 重命名文件，或移动文件
os.rename('aa.txt','bb.txt')

# 移动文件
os.rename('bb.txt','E:/bb.txt')


print(r)
