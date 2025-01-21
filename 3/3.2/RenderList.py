from typing import List

class RenderList:
    def __init__(self, type_list: str) -> None:
        self.type_list = type_list if type_list == "ol" else "ul"

    def __call__(self, lst: List[str], *args, **kwargs) -> str:
        list_items = [f'<li>{list_item}</li>' for list_item in lst]
        return (f'<{self.type_list}>\n'
                f'{"".join(list_items)}\n'
                f'</{self.type_list}')




########################################################################################################################

render = RenderList(type_list)

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)