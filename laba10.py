import json

def z1():
    with open('prr.json', mode='r', encoding='utf-8') as file:
        data = json.load(file)

    for prod in data['products']:
        if prod['available']:
            avi = 'В наличии'
        else:
            avi = 'Нет в наличии!'
        print(f"Название: {prod['name']}")
        print(f"Цена: {prod['price']}")
        print(f"Вес: {prod['weight']}")
        print(avi)


def z2():
    n_prod = {}
    n_prod["name"] = input("Название продукта: ")
    n_prod["price"] = input("Цена продукта: ")
    n_prod["weight"] = input("Вес продукта: ")
    avi = input("Есть ли он да или нет: ")
    if avi == "да":
        n_prod["available"] = True
    else:
        n_prod["available"] = False

        with open('prr.json', mode='r', encoding='utf-8') as file:
            data2 = json.load(file)
        data2["products"].append(n_prod)
        file.close()

        with open('products.json', mode='w', encoding='utf-8') as file:
            json.dump(data2, file)
            file.close()

    with open('products.json', mode='r', encoding='utf-8') as file:
        data = json.load(file)

    for prod in data['products']:
        if prod['available']:
            avi = 'В наличии'
        else:
            avi = 'Нет в наличии!'
        print(f"Название: {prod['name']}")
        print(f"Цена: {prod['price']}")
        print(f"Вес: {prod['weight']}")
        print(avi)

def z3():
    ru_en = {}
    with open('en-ru.txt', 'r', encoding='utf-8') as f:
        for line in f:
            p = line.strip().split('-')
            if len(p) == 2:
                en_word = p[0].strip()
                ru_words = p[1].strip().split(', ')
                for i in ru_words:
                    if i in ru_en:
                        ru_en[i].append(en_word)
                    else:
                        ru_en[i] = [en_word]
    with open('ru-en.txt', 'w', encoding='utf-8') as f:
        for i, en_word in ru_en.items():
            f.write(f"{i} - {en_word}\n")
z3()
