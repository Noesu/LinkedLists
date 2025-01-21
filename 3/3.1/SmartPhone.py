from typing import List, Union


class AppVK:
    def __init__(self) -> None:
        self.name = "ВКонтакте"

class AppYouTube:
    def __init__(self, memory_max: int) -> None:
        self.name = "YouTube"
        self.memory_max = memory_max

class AppPhone:
    def __init__(self, phone_list: dict) -> None:
        self.name = "Phone"
        self.phone_list = phone_list

class SmartPhone:
    def __init__(self, model: str) -> None:
        self.model = model
        self.apps: List[Union[AppVK, AppYouTube, AppPhone]] = []

    def add_app(self, app: Union[AppVK, AppYouTube, AppPhone]) -> None:
        for installed_app in self.apps:
            if installed_app.name == app.name:
                return
        self.apps.append(app)

    def remove_app(self, app: Union[AppVK, AppYouTube, AppPhone]) -> None:
        for installed_app in self.apps:
            if installed_app.name == app.name:
                self.apps.remove(installed_app)
                return


########################################################################################################################

sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)



# class SmartPhone:
#     def __init__(self, model):
#         self.model, self.apps = model, []
#     def add_app(self, app):
#         if app.__class__ not in (i.__class__ for i in self.apps):
#             self.apps.append(app)
#     def remove_app(self, app):
#         self.apps.remove(app) if app in self.apps else ...
#
# class AppVK:
#     def __init__(self, name = "ВКонтакте"):
#         self.name = name
# class AppYouTube:
#     def __init__(self, memory_max, name = "YouTube"):
#         self.name, self.memory_max = name, memory_max
# class AppPhone:
#     def __init__(self, phone_list: dict, name = "Phone"):
#         self.name, self.phone_list = name, phone_list