"""
    字典
        使用{}来创建字典
        字典的值可以是任意对象
        字典的键可以是任意的不可变的对象（int，str，bool，tuple...），但一般使用的是str
        字典的键是不能重复的，如果出现重复的后边的会替换到前边的
    语法一：
        {key:value,key:value,key:value,...}
    语法二：
        使用dict函数来创建字典
        dict(key=value,key=value,key=value,...)
        每一个参数都是一个键值对，参数名就是键，参数名就是值（这种方式创建的字典，key都是字符串）

"""
# 使用{}创建字典
d = {
    'name':'kevin',
    'age':23,
    'gender':'男',
    'name':'Mr.Cao'
}

print(d, type(d))

# 根据键来获取值
print(d['name'],d['age'],d['gender'])

# 如果使用了字典中不存在的键，会报错
# print(d['hello'])

# 使用dict()函数创建字典
d = dict(name='Mr.Cao',age=23,gender='男')
print(d)

# 也可以将一个包含有双值子序列转换为字典，双值序列，序列中只有两个值，[1,2] ('a',3) 'ab'
# 子序列，如果序列中的元素也是序列，那么我们就称这个元素为子序列



