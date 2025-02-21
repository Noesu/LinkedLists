from typing import Tuple

class Ingredient:
    def __init__(self, name: str, volume: float, measure: str) -> None:
        self.measure = measure
        self.volume = volume
        self.name = name

    def __str__(self) -> str:
        return f'{self.name}: {self.volume}, {self.measure}'

class Recipe:
    def __init__(self, *ingredients: Ingredient) -> None:
        self.ings = list(ingredients)

    def __len__(self) -> int:
        return len(self.ings)

    def add_ingredient(self, ing: Ingredient) -> None:
        if isinstance(ing, Ingredient):
            self.ings.append(ing)

    def remove_ingredient(self, ing: Ingredient) -> None:
        if ing in self.ings:
            self.ings.remove(ing)

    def get_ingredients(self) -> Tuple[Ingredient, ...]:
        return tuple(self.ings)


########################################################################################################################

recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe) # n = 3