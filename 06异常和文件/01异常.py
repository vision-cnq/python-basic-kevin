print('hello')
try:
    # try中放置的是有可能出现错误的代码
    print(10/0)
except:
    # except中放置的是出错之后的处理方案
    print('发生异常...')
else:
    print('程序没有异常...')
print('world')
