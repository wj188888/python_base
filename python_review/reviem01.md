## 继承
存取器方法（get_name和set_name）
然后(property)是一种功能强大的存取器替代品

- 对所有以两个下划线的名称开头的都会进行转换，开头加上
一个下划线和类名。
`ClassName._ClassName_funcName`
- `from module import *`不会导入以一个下划线打头的名称

## 类的命名空间
定义类时情况亦如此：在class语句中定义的代码都是在一个特殊的命名空间（类的命名空间）内执行的，
而类的所有成员都可访问这个命名空间

- 一个类访问自己的基类__base__
- 判断变量是否是某一个类的实例
    - `isinstance(s, Filter)`
- 访问属性是否存在
    - `hasattr(tc,'fond)`,tc是类的一个实例对象
    - `getattr(tc,'fond)`,获取tc实例的属性
    - `setattr(tc,'name', 'wangjie')` 设置属性name的值

## python抽象基类
其他语言都显示的指定接口的理念，而有些第三方模块提供了这种理念的这种实现。
python也引入了abc提供官方解决方案；这个模块是对抽象基类提供了支持

