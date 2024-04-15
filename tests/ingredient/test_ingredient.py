from src.models.ingredient import (Ingredient, Restriction)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    carne = Ingredient("carne")
    carne2 = Ingredient("carne")
    gorgonzola = Ingredient("queijo gorgonzola")
    assert hash(carne) == hash(carne2)
    assert hash(carne) != hash(gorgonzola)
    assert carne == carne2
    assert carne != gorgonzola
    assert carne.__repr__() == "Ingredient('carne')"
    tomate = Ingredient("tomate")
    assert tomate.name == "tomate"
    for restriction in carne.restrictions:
        assert restriction in {
            Restriction.ANIMAL_DERIVED, Restriction.ANIMAL_MEAT}

    tomate_restrictions = list(tomate.restrictions)
    assert len(tomate_restrictions) == 0
