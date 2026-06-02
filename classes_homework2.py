class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str) -> None:
        self.name = name
        self.quantity = quantity
        self.unit = unit
    
    @property
    def quantity(self) -> float:
        return self._quantity
    
    @quantity.setter
    def quantity(self, value: float) -> None:
        if value < 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = value
    
    def __str__(self) -> str:
        return f"{self.name}: {self.quantity} {self.unit}"
    
    def __repr__(self) -> str:
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Ingredient):
            return False
        return (self.name == other.name and self.unit == other.unit)


class Recipe:
    def __init__(self, title: str, ingredients: list) -> None:
        self.title = title
        self.ingredients = ingredients
    
    def add_ingredient(self, ingredient: Ingredient) -> None:
        for ing in self.ingredients:
            if ing == ingredient:
                ing.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)
    
    @staticmethod
    def is_valid_ratio(ratio) -> bool:
        if isinstance(ratio, (int, float)):
            return ratio > 0
        return False
    
    def scale(self, ratio: float) -> "Recipe":
        if not self.is_valid_ratio(ratio):
            raise ValueError("ratio должен быть положительным числом")
        mult_ing = []
        for i in self.ingredients:
            mult_ing.append(Ingredient(i.name, i.quantity * ratio, i.unit))
        new_recipe = Recipe(self.title, mult_ing)
        return new_recipe
    
    def __len__(self) -> int:
        return len(self.ingredients)
    
    def __str__(self) -> str:
        res = f"{self.title}:\n"
        for i in self.ingredients:
            res += f"  - {i}\n"
        return res