def get_shop_list_from_dishes(dishes, person_count):
    ingridients = {}
    for dish in dishes:
        if dish in cook_book:
            for ingridient in cook_book[dish]:
                if ingridient["ingridient_name"] in ingridients:
                    ingridients[ingridient["ingridient_name"]]["quanity"] += ingridient["quanity"] * person_count  
                else:                                                                                             
                    ingridients[ingridient["ingridient_name"]] = {                                                
                                                                 "measure": ingridient["measure"].strip(),                
                                                                 "quanity": ingridient["quanity"] * person_count                 
                                                                 }                                                                                 
    # ingridient in cook_book[dish] - итерация по списку словарей,
    # содержащих информацию об ингридиенте блюда
    # ingridients[ingridient["ingridient_name"]]["quanity"] - обращение
    # к внутреннему словарю, вложенному в словарь созданный внутри функции
    # по тому же значению, что уже лежит в словаре ingridient под ключом
    # "ingridient_name"
    # ingridients[ingridient["ingridient_name"]]["quanity"] += ingridient["quanity"] * person_count
    # это прибавление количетсва ингридиента, необходимого для блюда,
    # и умноженного на количество людей person_count, к уже имеющемуся количетву,
    # которое и лежит во "внутреннем словаре"
    # ingridients == {'Картофель': {'measure': кг, 'quanity': 2}}
    #                              ^                          ^
    #                     "Внутренний словарь"         Воооооооот сюда
        else:
            print("Искомого блюда нет в книге рецептов")
            return {}
    return ingridients

cook_book = {}
with open("recipes.txt", "r", encoding="utf-8") as recipebook:
    for line in recipebook:
        dish_name = line.strip()
        cook_book[dish_name] = []
        ingridient_amount = recipebook.readline()
        for ingridient in range(int(ingridient_amount)):
            ingridient = recipebook.readline()
            listed_ingredient = ingridient.split(" | ")

            ingridient_name = listed_ingredient[0]
            quanity = int(listed_ingredient[1])
            measure = listed_ingredient[2]

            cook_book[dish_name] += [{"ingridient_name": ingridient_name, 
                                    "quanity": quanity, 
                                    "measure": measure}]
        blank = recipebook.readline()
print(get_shop_list_from_dishes(["Омлет"], 4))
