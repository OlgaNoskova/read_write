from pprint import pprint
def dict_cook():
    with open("recipes.txt", encoding="UTF-8") as f:
        cook_book = {}
        for line in f.read().split('\n\n'):
            cook_list = line.split("\n")
            cook_name, cook_number = cook_list[0], int(cook_list[1])
            recipe_ = []
            food_recipe = {}
            for i in range(2, cook_number+2):
                ingredient = cook_list[i].split(' | ')
                ingredient_name = ingredient[0]
                quantity = ingredient[1]
                measure = ingredient[2]
                cook_ingredients = {}
                cook_ingredients['ingredient_name'] = ingredient_name
                cook_ingredients['quantity'] = quantity
                cook_ingredients['measure'] = measure
                recipe_.append(cook_ingredients)
            cook_book[cook_name] = recipe_
        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    ingredient_for_buy = {}
    for dish in dishes:
        if dish in cook:
            ingredients = cook[dish]
            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity']
                quantity_dict = {}
                if ingredient_name not in ingredient_for_buy.keys():
                    quantity_dict['measure'] = measure
                    quantity_dict['quantity'] = int(quantity) * person_count
                    ingredient_for_buy[ingredient_name] = quantity_dict
                else:
                    ingredient_for_buy[ingredient_name]['quantity'] += int(quantity) * person_count
    return ingredient_for_buy


cook = dict_cook()

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
