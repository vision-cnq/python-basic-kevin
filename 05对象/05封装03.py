'''
    property装饰器，用来将一个get方法，转换成对象的属性
        添加为property装饰器后，就可以像调用属性一样使用get方法
        使用property装饰的方法，必须和属性名是一样的
    setter方法的装饰器：
        @属性名.setter
'''
class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    @property
    def name(self):
        print('get方法执行了...')
        return self._name

    @name.setter
    def name(self, name):
        print('setter方法调用了')
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

p = Person('COCO',20)

p.name = 'KEVIN'
p.age = 23

print(p.name, p.age)






