import pytest
from classes_homework2 import Ingredient, Recipe, ShoppingList


#Тесты для класса Ingredient
def test_ingredient_creation():
    ing = Ingredient("что-то", 100.0, "гр")
    assert ing.name == "что-то"
    assert ing.quantity == 100.0
    assert ing.unit == "гр"

def test_ingredient_str():
    ing = Ingredient("что-то", 100.0, "гр")
    assert str(ing) == "что-то: 100.0 гр"

def test_ingredient_repr():
    ing = Ingredient("сахар", 100.0, "гр")
    assert repr(ing) == "Ingredient('сахар', 100.0, 'гр')"

def test_ingredient_eq():
    ing1 = Ingredient("сахар", 100.0, "гр")
    ing2 = Ingredient("сахар", 200.0, "гр")
    ing3 = Ingredient("соль", 100.0, "гр")
    ing4 = Ingredient("сахар", 100.0, "кг")
    assert ing1 == ing2
    assert ing1 != ing3
    assert ing1 != ing4


#Тесты для класса Recipe
def test_recipe_creation():
    ing1 = Ingredient("сахар", 100.0, "гр")
    ing2 = Ingredient("соль", 50.0, "гр")
    rec = Recipe("сахарсоль", [ing1, ing2])
    assert rec.title == "сахарсоль"
    assert len(rec.ingredients) == 2
    assert rec.ingredients[0] == ing1
    assert rec.ingredients[1] == ing2

def test_recipe_add_ingredient():
    ing1 = Ingredient("сахар", 100.0, "гр")
    ing2 = Ingredient("мука", 50.0, "гр")
    rec = Recipe("блинчик", [ing1])
    rec.add_ingredient(ing2)
    assert len(rec.ingredients) == 2
    assert rec.ingredients[1] == ing2

def test_recipe_add_existing_ingredient():
    ing1 = Ingredient("сахар", 100.0, "гр")
    ing2 = Ingredient("сахар", 50.0, "гр")
    rec = Recipe("сахарная вата", [ing1])
    rec.add_ingredient(ing2)
    assert len(rec.ingredients) == 1
    assert rec.ingredients[0].quantity == 150.0

def test_recipe_scale():
    ing1 = Ingredient("сахар", 100.0, "гр")
    ing2 = Ingredient("мука", 50.0, "гр")
    rec = Recipe("блинчик", [ing1, ing2])
    sc_rec = rec.scale(2)
    assert sc_rec is not rec
    assert sc_rec.title == "блинчик"
    assert sc_rec.ingredients[0].quantity == 200.0
    assert sc_rec.ingredients[1].quantity == 100.0

def test_recipe_scale_invalid_ratio():
    ing1 = Ingredient("сахар", 100.0, "гр")
    rec = Recipe("сахарная вата", [ing1])
    with pytest.raises(ValueError):
        rec.scale(-1)
    with pytest.raises(ValueError):
        rec.scale(0)

def test_recipe_len():
    ing1 = Ingredient("сахар", 100.0, "гр")
    rec = Recipe("сахарная вата", [ing1])
    ing2 = Ingredient("сахар", 50.0, "гр")
    assert len(rec) == 1


#Тесты для класса ShoppingList
def test_shopping_list_add_recipe():
    ing1 = Ingredient("Сахар", 100.0, "гр")
    rec = Recipe("Пирожное", [ing1])
    sl = ShoppingList()
    sl.add_recipe(rec, 2)
    assert len(sl._items) == 1
    assert sl._items[0][0].quantity == 200.0
    assert sl._items[0][1] == "Пирожное"
    with pytest.raises(ValueError):
        sl.add_recipe(rec, -1)

def test_shopping_list_remove_recipe():
    ing1 = Ingredient("Сахар", 100.0, "гр")
    rec = Recipe("Пирожное", [ing1])
    sl = ShoppingList()
    sl.add_recipe(rec, 2)
    sl.remove_recipe("Пирожное")
    assert len(sl._items) == 0

def test_shopping_list_remove_nonexist():
    ing1 = Ingredient("Сахар", 100.0, "гр")
    rec = Recipe("Сахар", [ing1])
    sl = ShoppingList()
    sl.add_recipe(rec, 2)
    sl.remove_recipe("Привет если кто-то смотрит")
    assert len(sl._items) == 1

def test_shopping_list_get_list_is_sorted():
    ing1 = Ingredient("а", 100.0, "гр")
    ing2 = Ingredient("б", 100.0, "гр")
    ing3 = Ingredient("в", 100.0, "гр")
    rec1 = Recipe("сахар1", [ing1])
    rec2 = Recipe("сахар2", [ing2])
    rec3 = Recipe("сахар3", [ing3])
    sl = ShoppingList()
    sl.add_recipe(rec1, 2)
    sl.add_recipe(rec2, 1)
    sl.add_recipe(rec3, 3)
    shopping_list = sl.get_list()
    assert shopping_list[0].name == "а"
    assert shopping_list[1].name == "б"
    assert shopping_list[2].name == "в"

def test_shopping_list_get_list():
    ing1 = Ingredient("сахар", 100.0, "гр")
    rec1 = Recipe("сахар", [ing1])
    rec2 = Recipe("сахар", [ing1])
    sl = ShoppingList()
    sl.add_recipe(rec1, 2)
    sl.add_recipe(rec2, 3)
    shopping_list = sl.get_list()
    assert len(shopping_list) == 1
    assert shopping_list[0].name == "сахар"
    assert shopping_list[0].quantity == 500.0

def test_shopping_list_add():
    ing1 = Ingredient("сахар", 100.0, "гр")
    rec1 = Recipe("сахар", [ing1])
    rec2 = Recipe("мука", [ing1])
    sl1 = ShoppingList()
    sl2 = ShoppingList()
    sl1.add_recipe(rec1, 2)
    sl2.add_recipe(rec2, 3)
    sl3 = sl1 + sl2
    assert len(sl3._items) == 2
    assert sl1.get_list() == [(Ingredient("сахар", 200.0, "гр"))]
    assert sl2.get_list() == [(Ingredient("сахар", 300.0, "гр"))]