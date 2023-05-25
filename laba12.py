from tkinter import *

def z1():
    class icecream:
        def __init__(self, ice_name, type, flavors):
            self.ice_name = ice_name
            self.type = type
            self.flavors = flavors

        def disp_flavors(self):
            print("Сорта мороженого:")
            for flavor in self.flavors:
                print(f"Мороженое {flavor}")

    icecreamstand = icecream("РОЖОК", "Мороженое", ["Шоколадное", "Ванильное", "Клубничное"])
    icecreamstand.disp_flavors()

def z2():
    flavors = ["шоколадное", "ванильное", "клубничное", "мятное"]
    dictionary = {"Мягкое": flavors, "Стаканчик": flavors, "На палочке": flavors}

    class icecream:
        def __init__(self, ice_name, type, flavors, location, time):
            self.ice_name = ice_name
            self.type = type
            self.flavors = flavors
            self.location = location
            self.time = time

        def disp_flavors(self):
            print("Сорта мороженого:")
            for flavor in self.flavors:
                print(f"Мороженое {flavor}")

        def disp_location(self):
            print (f'{self.ice_name} - {self.location}:  проспект Ударников')

        def disp_time(self):
            print (f'{self.ice_name} - {self.time}: работает с 10:00 до 20:00')

        def add_flavor(self):
            kol = input("Сколько вкусов хотите добавить? ")
            while int(kol) > 0:
                n = input("Введите мороженое: ")
                flavors.append(n)
                kol = int(kol) - 1

        def del_flover(self,):
            kol = input("Сколько вкусов хотите убрать? ")
            while int(kol) > 0:
                n = input("Введите мороженое: ")
                flavors.remove(n)
                kol = int(kol) - 1

        def check_flavor(self):
            w = (input("Введите мороженное для проверки: ") in flavors)
            if w == True:
                print("В наличии")
            else:
                print("Нет в наличии")

        def stick(self):
            print("У нас есть мороженое на палочке")
            r = input("Хотите ли мороженное на палочке? ")
            if r == 'да':
                print('Держи')

        def soft(self):
            print("У нас есть мягкое мороженое")
            r = input("Хотите ли мягкое мороженное? ")
            if r == 'да':
                print('Лови')

        def cup(self):
            print("У нас мороженое в стаканчике")
            r = input("Хотите ли мороженное в стаканчике? ")
            if r == 'да':
                print('НАААА')

    icecreamstand = icecream("РОЖОК", "Мороженое",
                         ["шоколадное", "ванильное", "клубничное", "мятное"], 'Расположение', 'Время')
    icecreamstand.disp_flavors()
    icecreamstand.disp_location()
    icecreamstand.disp_time()
    icecreamstand.add_flavor()
    icecreamstand.del_flover()
    icecreamstand.check_flavor()
    icecreamstand.cup()
    icecreamstand.soft()
    icecreamstand.stick()

def z3():
    class icecream:
        def __init__(self, ice_name, type, flavors):
            self.ice_name = ice_name
            self.type = type
            self.flavors = flavors

        def disp_flavors(self):
            print("Сорта мороженого:")
            for flavor in self.flavors:
                print(f"мороженое {flavor}")

        def frame(self):
            root = Tk()
            root.geometry("512x512")
            root.title("Мороженое")
            for f in self.flavors:
                item = Label(text = f, font=7)
                item.pack()
            root.mainloop()

    icecreamstand = icecream("РОЖОК", "Мороженое",
                             ["Шоколадное", "Ванильное", "Клубничное", "Мятное"])
    icecreamstand.disp_flavors()
    icecreamstand.frame()

