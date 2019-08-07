class Dog:
    '''
        表示狗的类
    '''
    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def jiao(self):
        '''
            狗叫的方法
        :return:
        '''
        print('汪汪汪...')

    def yao(self):
        '''
            狗咬的方法
        :return:
        '''
        print('咬人...')

    def run(self):
        print('%s 快乐的奔跑着...' %self.name)

# 创建类的实例
d = Dog('小黑',8,'male',30)

# 目前我们可以直接通过 对象.属性的方式来修改属性的值，这种方式导致对象中的属性可以随意修改
# 但是这种方式修改值并不安全，而且值可以任意修改，不论对错
# 现在我们就需要一种方式来增强数据的安全性
# 1. 属性不能属于修改（我让你改你才能改，不让你改你就不能改）
# 2. 属性不修改为任意的值（比如：年龄不能是负数）

d.name = '阿黄'
d.age = -10
d.run()
print(d.age)





