print("Задание 1")

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан {self.name} : {self.cuisine_type} кухня")

    def open_restaurant(self):
        print(f"Ресторан {self.name} открыт!")


new_restaurant = Restaurant("Столовая №1", "Домашняя")
print(new_restaurant.name)
print(new_restaurant.cuisine_type)
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()

print("Задание 2")

restaurant1 = Restaurant("KFC", "Фаст фуд")
restaurant2 = Restaurant("Доски", "Русская")
restaurant3 = Restaurant("Чача", "Грузинская")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

print("Задание 3")

class Restaurant:
    def __init__(self, name, cuisine_type, rating):
        self.name = name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Ресторан {self.name} : {self.cuisine_type} кухня")

    def open_restaurant(self):
        print(f"Ресторан {self.name} открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана {self.name} был обновлен до {self.rating}.")


new_restaurant = Restaurant("Чикен пицца", "фаст фуд", 4.5)
new_restaurant.update_rating(int(input("Введите новый рейтинг: ")))


