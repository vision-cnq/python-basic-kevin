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

    获取字典中的值，根据键来获取值
        语法：
            dict[key]
        通过[]来获取值时，如果键不存在，会抛出异常KeyError

    get(key[,default])
        该方法用来根据键来获取字典中的值，如果获取的键在字典中不存在，会返回第二个参数，这样获取不到值时，会返回默认值

    修改字典
        dict[key] = value，如果key存在则覆盖，不存在则添加

    setdefault(key[,default])
        可以用来向字典中添加key-value，key 存在则返回值，key不存在则添加key

    update([other])
        将其他的字典中的key-value添加到当前的字典中，有重复的key，则覆盖原本的

    del dict[key]
       删除,可以使用del来删除字典中的key-value

    popitem()
        随机删除字典中的一个键值对，一般会删除最后一个键值对，删除后，会将删除的key-value作为返回值返回
        返回的是一个元组，元组中有两个元素，第一个元素是删除的key，第二个元素是删除的value
        当使用popitem()删除一个空字典时，会抛出异常 KeyError：'popitem(): dictionary is empty'

    pop(key[,default])
        根据key删除字典中的key-value，会将被删除的value返回，
        如果删除不存在的key，会抛出异常，
        如果指定了默认值，再删除不存在的key，则不会抛出异常，并返回默认值

    clear()
        清空字典

    copy()
        复制，该方法用于对字典进行浅复制，复制以后的对象和原对象是独立，修改一个不会影响一个
        注：浅复制会简单复制对象内部的值，如果值也是一个可变对象，这个对象不会被复制

    遍历字典
        keys()
            该方法返回字典的所有key，返回一个序列，序列中保存字典的所有key

        values()
            该方法返回字典的所有value，返回一个序列，序列中保存字典的所有value

        items()
            该方法返回字典中所有的项，返回一个序列，序列中包含双值子序列，分别是key和value

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
# [(1,2),(3,5)]
d = dict([('name','Mr.Cao'),('age',23)])
print(d)

d = dict(name='Mr.Cao',age=23,gender='男')

# len()获取字典中键值对的个数
print(len(d))

# in 检查字典中是否包含指定的键
# not in 检查字典中是否不包含指定的键
print('hello' in d)

# 获取字典中的值，根据键来获取值
print(d['age'])

# 通过get(key[,default])获取键来获取字典的值
print(d.get('name'))
print(d.get('hello','默认值'))     # 没有hello，则返回默认值

# 修改字典 d[key]
d['name'] = 'KEVIN'     # 修改字典的key-value
d['address'] = '广州'     # 向字典中添加key-value
print(d)

# setdefault(key[,default]) 可以向字典中添加key-value
result = d.setdefault('name','Mr.Cao')  # 存在，则返回key的值
result = d.setdefault('hello','world')  # 不存在，添加key
print(result)

# update([other]) 将其他的字典中key-value添加当前字典中，有重复的key，则覆盖
d1 = {'a':1,'b':2,'c':3}
d2 = {'d':4,'e':5,'a':7}    # 'a':7，替换掉'a':1
d1.update(d2)
print(d1)

# del，删除字典的key-value
del d1['a']
del d1['b']
print(d1)

# popitem() 随机删除并以元组方式返回删除的key-value，一般会删除最后一个键值对
result = d1.popitem()
print(result)

# pop[key[,default]，根据key删除字典中的key-value，并返回value
result = d.pop('age')
result = d.pop('xxx','默认值')
print(result)

# clear() 清空字典
d.clear()
print(d)

# copy()复制字典
d2 = d1.copy()
print(d2)

# 创建字典
d = {'a':{'name':'KEVIN','age':23},'b':2,'c':3}
d2 = d.copy()       # 复制字典
d2['a']['name'] = 'Mr.cao' # 修改值
# 对比对象的地址值
print('d = ',d,id(d))
print('d2 = ',d2,id(d2))

d = {'name':'Mr.Cao','age':23,'gender':'男'}
print('-'*64)

# 通过遍历keys()获取所有的键
for k in d.keys() :
    print('key = ',k,', value = ',d[k])

print('-'*64)

# 通过遍历values()获取所有的值
for v in d.values() :
    print('value = ',v)

print('-'*64)

# 通过遍历items()获取所有的的key，value
for k,v in d.items() :
    print(k,' = ',v)
