# 格式化字符串
a = 'hello'

# 字符串不能用加号与别的类型进行拼接
a = 'ab'+'cd'+'ef'
print("a = " + a)   # 该写法在python不常见
a = 123
print('a =',a)      # 一般是这样写
print(a)

# 在创建字符串时，可以在字符串中指定占位符
# %s 在字符串中表示任意字符
# %f 浮点数占位符
# %d 整数占位符
b = 'Hello %s'%'孙悟空'
print(b)
b = 'hello %s 你好 %s'%('tom','孙悟空')
print(b)
b = 'hello %3.5s'%'abcdefg' # %3.5s字符串的长度限制在3-5之间
print(b)
b = 'hello %s'%123.456
print(b)
b = 'hello %.2f'%123.456
print(b)
b = 'hello %d'%123.95
print(b)
b = '呵呵'
print(b)

# 在字符串前添加一个f来创建一个格式化字符串可以直接嵌入变量
c = f'hello {a} {b}'
print(c)

# 字符串的复制（将字符串和数字相乘）
a = 'abc'
# 如果将字符串和数字相乘，则解释器会将字符串重复指定的次数并返回
a = a * 20
print(a)


# 创建一个变量来保存你的名字
name = 'Mr.Cao'

# 使用四种方式来输出，欢迎 xxx 光临
# 拼串
print('欢迎 '+name+' 光临！')
# 多个参数
print('欢迎',name,'光临！')
# 占位符
print('欢迎 %s 光临！'%name)
# 格式化字符串
print(f'欢迎 {name} 光临！')







