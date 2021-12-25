# 需求：
#

import numbers

# 让两种Field都可以使用这个，在ModelMetaClass的__new__中不需要做判断了
class Field:
    pass

class IntField(Field):
    # 进行初始化设置
    def __init__(self, db_column, min_value=None, max_value=None):
        self._value = None
        self.min_value = min_value
        self.max_value = max_value
        self.db_column = db_column

        if min_value is not None:
            if not isinstance(min_value, numbers.Integral):
                raise ValueError("min_value must be int")
            elif min_value < 0:
                raise ValueError("min_value must be positive int")
        if max_value is not None:
            if not isinstance(max_value, numbers.Integral):
                raise ValueError("max_value must be int")
            elif max_value > 100:
                raise ValueError("max_value must be positive int")
        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise ValueError("min_value is must be smaller than max_value")
                min_value, max_value = max_value, min_value

    # 数据描述符
    def __get__(self, instance, owner):
        return self._value
    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < self.min_value or value > self.max_value:
            raise ValueError("value must between min_value and max_value")
        self._value = value


class CharField(Field):
    def __init__(self, db_column, max_length=None):
        self.value = None
        self.db_column = db_column

        if max_length is None:
            raise ValueError("you must spcify max_length for charfiled")
        self.max_length = max_length

    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('value must be string')
        if len(value) > self.max_length:
            raise ValueError("value len excess len of max_length")


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        if name == "BaseModel":
            return super().__new__(cls, name, bases, attrs, **kwargs)
        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key]= value
        attrs_meta = attrs.get("Meta", None)
        _meta = {}
        db_table = name.lower()
        if attrs_meta is not None:
            table = getattr(attrs_meta, "db_table", None)
            if table is not None:
                db_table = table
        _meta["db_table"] = db_table
        attrs["_meta"] = _meta
        attrs["fields"] = fields
        del attrs["Meta"]
        return super().__new__(cls, name, bases, attrs, **kwargs)


class BaseModel(metaclass=ModelMetaClass):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return super().__init__()

    def save(self):
        fields = []
        values = []
        for key, value in self.fields.items():
            db_column = value, db_column
            if db_column is None:
                dn_column = key.lower()
            fields.append(db_column)
            value = getattr(self, key)
            values.append(str(value))
        sql = f"insert {db_column}({fields}) value({values}))".format(self._meta["db_table"], fields=",".join(fields), values=",".join(values))

        pass
class User(BaseModel):

    # 给数据表映射一个最大长度
    name = CharField(db_column="", max_length=10)   # 这些是表的列
    age = IntField(db_column="", min_value=0, max_value=100)

    class Meta:
        db_table = ""

if __name__ == '__main__':
    user = User()
    user.name = "bobby"
    user.age = 28
    user.save()