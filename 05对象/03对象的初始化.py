"""
    魔术方法
        在类中可以定义一些特殊的方法（魔术方法）
    特殊方法都是__开头，__结尾的方法
    特殊方法不需要我们自己调用，不要尝试去调用特殊方法
    特殊方法将会在特殊的时刻自动调用
    学习特殊方法：
        1.特殊方法什么时候调用
        2.特殊方法有什么作用
    创建对象的流程
        p1 = Person()的运行流程
            1.创建一个变量
            2.在内存中创建一个新对象
            3.__init__(self)方法执行
            4.将对象的id赋值给变量
    init会在对象创建以后立刻执行
    init可以用来向新创建的对象中初始化属性
    调用类创建对象时，类后边的所有参数都会依次传递到init()中

"""
class Person :
    # 创建魔术方法
    def __init__(self,name):
        # print(self)
        # 通过self向新建的对象中初始化属性
        self.name = name

    def say_hello(self):
        print('大家好，我是%s'%self.name)

# p1 = Person() # 抛出异常
# 手动向对象添加name属性
# p1.name = 'KEVIN'

# 由于新建了一个__init__方法，且在里面有一个name属性，所有在创建的时候，需要有参数
p1 = Person('KEVIN')
p2 = Person('COCO')
p3 = Person('MrCao')
p4 = Person('CNQ')

print(p1.name)
print(p2.name)
print(p3.name)
print(p4.name)

p4.say_hello()

