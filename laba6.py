def z1():
    countries = {
        "Россия": "Москва",
        "Франция": "Париж",
        "США": "Вашингтон",
        "Германия": "Берлин",
    }
    print("Словарь стран: ", *countries)
    v = input("Выбор страны: ")
    print("Столица выбранной страны: ", countries[v])
    print("Отсортированный словарь: ", *sorted(countries))

def z2():
    ball = {
        1: ['а', "б", "в", "г", "д"],
        2: ['д', "е", "ё", "ж", "з"],
        3: ['и', "й", "к", "л", "м"],
        4: ['н', "о", "п", "р", "с"],
        5: ['т', "у", "ф", "х", "ц"],
        6: ['ч', "щ", "ъ", "ы", "ь"],
        7: ['э', "ю", "я"]
    }
    s = input("Введите слово: ")
    s = list(s)
    cnt = 0
    for i in s:
        for j in ball:
            if i in ball[j]:
                cnt += j
    print("Введенное слово стоит", cnt, "балла")

def z3():
    students = {
        1: ['rus', "eng", "ita"],
        2: ['spa', "ger", "chi"],
        3: ['ger', "chi", "spa"],
        4: ['ita', "eng", "rus"],
        5: ['chi', "rus", "ger"],
        6: ['ger', "eng", "ita"],
        7: ['rus', "chi", "spa"]
    }
    a = []
    b = []
    cnt = 0
    for i in students:
        for i in students[i]:
            if i not in a:
                a.append(i)
                cnt += 1
    for i in students:
        if "chi" in students[i]:
            b.append(i)
        else:
            continue
    print("Языки: ",*(sorted(a)))
    print("Количество языков: ", cnt)
    print("Знают китайский: ", *b)
