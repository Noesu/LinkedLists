from abc import ABC, abstractmethod

# здесь объявляйте классы

# class Transport(ABC):
#     @abstractmethod
#     def go(self):
#         """Метод для перемещения транспортного средства"""
#
#     @classmethod
#     @abstractmethod
#     def abstract_class_method(cls):
#         """Абстрактный метод класса"""
#
# class Bus(Transport):
#     def __init__(self, model, speed):
#         self._model = model
#         self._speed = speed
#
#     def go(self):
#         print("bus go")
#
#     @classmethod
#     def abstract_class_method(cls):
#         pass

########################################################################################################################

class Model(ABC):
    @abstractmethod
    def get_pk(self) -> int:
        pass

    def get_info(self):
        return "Базовый класс Model"

class ModelForm(Model):
    __id = 0

    def __init__(self, login: str, password: str) -> None:
        self._login = login
        self._password = password
        self._id = type(self).__id
        type(self).__id += 1

    def get_pk(self) -> int:
        return self._id





