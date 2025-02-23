Необходимо объявить функцию-декоратор _class_log_ для класса, которая бы создавала логирование вызовов методов класса. Например следующие строчки программы:
```python
vector_log = []

@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value
```
декорируют класс **Vector** и в список _vector_log_ добавляются имена методов, которые были вызваны при использовании этого класса. В частности, после выполнения команд:
```python
v = Vector(1, 2, 3)
v[0] = 10
```
в списке vector_log должны быть два метода:

`['__init__', '__setitem__']`

Ваша задача реализовать декоратор с именем _class_log_.

Напоминание. Ранее вы уже создавали функцию-декоратор для класса следующим образом:
```python
def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls
```
Используйте этот принцип для успешного прохождения подвига.

P.S. В программе нужно объявить только класс и необходимые функции. На экран выводить ничего не нужно.