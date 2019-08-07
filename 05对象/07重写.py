'''
    在子类中如果有和父类同名的方法，则通过子类实例去调用方法时，
        会调用子类的方法而不是父类的方法，这个特点称为方法的重写（覆盖，override）
    创建Dog类的实例

    当我们调用一个对象的方法时：
        会优先去当前对象中寻找是否具有该方法，如果有则直接调用，
        如果没有，则去当前对象的父类中寻找，如果父类中有则直接调用父类中的方法，
        如果还是没有，则去父类的父类去寻找，以此类推，直到找到object，依旧没有将抛出异常。




'''

# 使用继承，Animal为父类，Dog为子类，重写父类的run方法
class Animal:
    def run(self):
        print('动物会跑...')

    def sleep(self):
        print('动物睡觉...')

class Dog(Animal):
    def bark(self):
        print('狗在叫...')
    def run(self):
        print('狗在跑...')

d = Dog()
d.run()
d.sleep()


# 继承与重写
class A(object):
    def test(self):
        print('AAA')

class B(A):
    def test(self):
        print('BBB')

class C(B):
    def test(self):
        print('CCC')

# 创建一个c的实例
c = C()
c.test()











