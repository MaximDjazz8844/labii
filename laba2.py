def z5():

    print("Ввод слов")
    print(' '.join([input ('Введите слово: ') for i in range(int(input('Количество слов: ')))]))

def z4():

    print("Смеситель")
    a, b = input(), input()
    if a != 'красный' and a != 'желтый' and a != 'синий':
        print('ошибка цвета ')
    elif b != 'красный' and b != 'желтый' and b != 'синий':
        print('ошибка цвета ')
    elif a == 'красный' and b == 'синий' or b == 'красный' and a == 'синий':
        print('фиолетовый')
    elif a == 'красный' and b == 'желтый' or b == 'красный' and a == 'желтый':
        print('оранжевый')
    elif a == 'синий' and b == 'желтый' or b == 'синий' and a == 'желтый':
        print('зеленый')
    elif a == 'красный' and b == 'красный':
        print('красный')
    elif a == 'синий' and b == 'синий':
        print('синий')
    elif a == 'желтый' and b == 'желтый':
        print('желтый')

def z1():

    print("пароли")
    a = input()
    b = input()
    if a == b:
        print("пароль принят")
    else:
        print("пароль не принят")


def z2():

    print("места в вагоне")
    n = int(input('введите номер вашего места: '))
    print()
    if n > 36:
        print('ваше место - боковое.')
    elif n % 2:
        print('ваше место в купе внизу.')
    else:
        print('ваше место в купе наверху.')

def z3():

    print("проверка на год")
    year = int(input())
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print('високосный')
    else:
        print('не високосный')
