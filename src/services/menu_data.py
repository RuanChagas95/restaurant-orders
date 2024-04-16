import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = []

        with open(source_path, newline='') as csvfile:
            reader = list(csv.reader(csvfile))
        recipes = {}
        for index in range(1, len(reader)):
            name = reader[index][0]
            price = reader[index][1]
            ingredient = reader[index][2]
            amount = reader[index][3]
            if recipes.get(f'{name} - {price}') is None:
                recipes[f'{name} - {price}'] = [
                    {
                        'ingredient': ingredient,
                        'amount': amount
                    }
                ]
            else:
                recipes.get(f'{name} - {price}').append({
                    'ingredient': ingredient,
                    'amount': amount
                })
        for name_price, ingredients in recipes.items():
            name, price = name_price.split(' - ')
            dish = Dish(name, float(price))
            for ingredient in ingredients:
                dish.add_ingredient_dependency(Ingredient(
                    ingredient['ingredient']), int(ingredient['amount']))
            self.dishes.append(dish)
