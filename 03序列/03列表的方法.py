"""
    列表的方法
        append()：向列表的最后添加一个元素
        insert()：向列表的指定位置插入一个元素
        extend()：使用新的序列来扩展当前序列,需要一个序列作为参数，它会将该序列中的元素添加到当前列表中
        clear()：清空序列
        pop()：根据索引删除并返回被删除的元素
        remove()：删除指定值得元素，如果相同值得元素有多个，只会删除第一个
        reverse()：用来反转列表
        sort()：用来对列表中的元素进行排序，默认是升序排列，如果需要降序排列，则需要传递一个reverse=True作为参数

"""

#  创建列表
stus = ['牛魔王', '红孩儿', '红孩儿', '唐僧', '二郎神', '白骨精']
print('原列表: ', stus)

# 在列表的最后添加一个元素
stus.append('孙悟空')

# 在列表的指定位置插入一个元素
stus.insert(2,'这是个啥')

# 扩展当前序列
stus.extend(['哦吼','你是谁'])

# 清空序列
# stus.clear()

# 根据索引删除并返回被删除的元素
result = stus.pop(2)    # 删除索引为2的元素
result = stus.pop()     # 删除最后一个元素
print("result: ",result)

# 删除指定元素，如果相同指定元素有多个，只会删除第一个元素
stus.remove('哦吼')

# 反转列表
stus.reverse()

# 对列表的元素进行排序
stus.sort()     # 默认升序
stus.sort(reverse = True)     # 倒序



print(stus)













