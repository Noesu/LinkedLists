class InputValues:
    def __init__(self, render) -> None:
        self.__render = render

    def __call__(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            return list(map(self.__render, func(*args, **kwargs).split()))
        return wrapper

class RenderDigit:
    def __call__(self, string, *args, **kwargs):
        try:
            return int(string)
        except ValueError:
            return None


render = RenderDigit()
input_dg = InputValues(render)(input)
res = input_dg()
print(res)