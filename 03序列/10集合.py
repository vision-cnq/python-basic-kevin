"""
    集合
        方式一：使用{} 来创建集合，自动去重，默认升序

        方式二：set() 函数创建集合

        in和not in
            检查集合中的元素
        len()
            获取集合中元素的数量
        add()
            向集合中添加元素
        update()
            将一个集合中的元素添加当前集合，update()可以传递序列或字典作为参数，字典只会使用键
        pop()
            随机删除并返回一个集合中的元素
        remove()
            删除集合中的指定元素
        clear()
            清空集合
        copy()
            对集合进行浅复制

"""


s = {10,3,5,2,16,1,2,8,4,3}
print(s)

s = set()   # 空集合
# 通过set()可以将序列和字典转换为集合
s = set([1,2,3,4,5,78,5,3,4])   # 使用set()将列表转成集合
print(s)
s = set('hello')                # 使用set()将字符串转成集合
print(s)
s = set({'a':1,'b':2,'c':3})    # 使用set()将字典转换成集合时，只会包含字典中的键
print(s)

# 创建集合
s = {'a','b',1,2,3,2}

# 使用in和not in来检查集合中的元素
print('c' in s)

# 使用len()获取集合中元素的数量
print(len(s))

# 使用add()向集合中添加元素
s.add(10)
s.add(30)
print(s)

# update()将一个集合中的元素添加到当前集合中
s2 = set('hello')
s.update(s2)
s.update((10,20,30,40,50))
s.update({10:'ab',20:'bc',100:'cd',1000:'ef'})
print(s)

# pop()随机删除并返回一个集合中的元素
result = s.pop()

# remove()删除集合中的指定元素
s.remove(100)
s.remove(1000)

# copy()对集合进行浅复制
s2 = s.copy()
print('s = ',s,id(s))
print('s2 = ',s2,id(s2))

# clear()清空集合
s.clear()