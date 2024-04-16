import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import (Ingredient, Restriction)

# Req 2


def test_dish():
    with pytest.raises(TypeError):
        Dish("Pizza", "False")
    with pytest.raises(ValueError):
        Dish("Pizza", -10.1)
    pizza = Dish("Pizza", 10.1)
    assert pizza.name == "Pizza"
    assert pizza.price == 10.1
    pizza2 = Dish("Pizza", 10.1)
    assert pizza == pizza2
    assert hash(pizza) == hash(pizza2)
    hotdog = Dish("Hotdog", 5.0)
    assert pizza != hotdog
    assert hash(pizza) != hash(hotdog)

    assert pizza.__repr__() == "Dish('Pizza', R$10.10)"
    carne = Ingredient("carne")
    hotdog.add_ingredient_dependency(carne, 1)
    assert hotdog.get_ingredients() == {carne}
    assert hotdog.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT
    }
