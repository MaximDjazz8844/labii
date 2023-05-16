def  z1():
    a = [1, 2, 3, 4, 5, 6, 7]
    b = int(input("Введите число "))
    if b in a:
        print("Угадал")
    else:
        print("Не угадали")

def z2():
    c = []
    a = [7, 1, 2, 7, 5, 3, 6, 7, 1, 2]
    for b in a:
        if a.count(b) > 1:
            if b not in c:
                c.append(b)
    print(c)

def z3():
    dn = ('пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс')
    a = int(input("Введите количество выходных "))
    for b in dn:
        print("Рабочие: ", *dn[:-a])
        print("Выходные: ", *dn[-a:])
        break

def z4():
    import random
    s1 = ('аб', 'дн', 'ке', 'си', 'ле', 'жи', 'ве', 'ба', 'гу', 'зе')
    s2 = ('еп', 'уз', 'оп', 'ан', 'ид', 'ык', 'эо', 'юс', 'аб', 'ой')
    a1 = []
    a2 = []
    a = []
    a1.append(random.sample(s1, 5))
    a2.append(random.sample(s2, 5))
    a.extend(*a1)
    a.extend(*a2)
    a = tuple(a)
    print("Изначальный список 1: ", *s1)
    print("Изначальный список 2: ", *s2)
    print("Получившиейся кортеж: ", *a)
    print("Длина кортежа: ", len(a))
    print("Отсортированный кортеж: ", *sorted(a))
    print("Поиск элемента: ", "аб" in a)
    print("Количество элементов: ", a.count("аб"))

