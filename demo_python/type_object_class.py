# -- coding:utf-8 --
a= 1
b="acb"
xx= type(1)
yy = type(int)
'''
    1是int类的实例化对象，int是由type生成的，type是所有对象的类，int，str是type这个类的实例化；
'''
print(xx)
print(yy)

class Student():
    pass

stu=Student()
print(type(stu))    # <class '__main__.Student'>
print(type(Student))    # <class 'type'>

'''
    逻辑：type->int->1,type->list->[1,2],type->dict->{'name': "wj"}
    逻辑2：type->class->obj
    
    obj是一个基类的概念,object是最顶层的基类；
    加入MyStudent继承了Student，那么Student.__bases__,的结果是<class 'object'>
    MyStudent.__bases__,的结果是<class '__main__.Student'>
    
    type本身是一个类，当然type它也是一个对象;
    
    
    总结：
    1.type是一切的基类，除了object
    2.type自己也是自己的类，和实例
    3.type的实例是type自己和object
    4.所有其他对象都继承了object，包括type,因为这个特性，所有type的实例是自己，类也是自己
'''
print(type.__bases__)   # 是个元祖(<class 'object'>,)
print(type(object)) # <class 'type'>
print(object.__bases__) # ()为空的

