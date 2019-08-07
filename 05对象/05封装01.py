'''
    封装是面向对象的三大特性之一
    封装指的是隐藏对象中一些不希望被外部所访问到的属性或者方法
    如何隐藏一个对象中的属性
        将对象的属性名，修改为一个外部不知道的名字
    如果获取（修改）对象中的属性。
        需要提供getter和setter方法使外部可以访问的到属性
        getter 获取对象中的指定属性（get_属性名）
        setter 设置对象中的指定属性（set_属性名）
    使用封装，确实增加了类的定义的复杂程度，但它也确保了数据的安全性
        1.隐藏属性名，使调用者无法随意的修改对象中的属性
        2.增加了getter和setter方法，很好的控制的属性是否是只读
            如果希望属性是只读的，则可以直接去掉setter方法
            如果希望属性是不能被外部访问，则可以直接去掉getter方法
        3.使用setter方法设置属性，可以增加数据的验证，确保数据的值是正确的
        4.使用getter方法获取属性，使用setter方法设置属性
            可以在读取属性和修改属性的同时做一些其他的处理
        5.使用getter方法可以表示一些计算的属性
'''
class Dog:
    '''
        表示狗的类
    '''
    def __init__(self, name ,age):
        self.hidden_name = name
        self.hidden_age = age

    def say_hello(self):
        print('大家好，我是%s' %self.hidden_name)

    def get_name(self):
        '''
            get_name() 用来获取对象的name属性
        :return:
        '''
        return self.hidden_name

    def set_name(self,name):
        self.hidden_name = name

    def get_age(self):
        return self.hidden_age

    def set_age(self,age):
        if age > 0 :
            self.hidden_age = age

d = Dog('旺财',8)

d.say_hello()

# 调用setter来修改name属性
d.set_name('小黑')
d.set_age(-10)

d.say_hello()
print(d.get_name())
print(d.get_age())      # age在设置值的时候是-10，不符合，则没有被修改
