import csv
import os
from PIL import Image, ImageFilter

def z1():
    a = ('png')
    os.mkdir('new')
    for i in os.listdir():
         if i.endswith(a):
            with Image.open(i) as img:
                img2 = img.filter(ImageFilter.CONTOUR)
            img2.save('new/' + str(i))

def z2():
    a = ('.jpg', '.png')
    os.mkdir('new2')
    for i in os.listdir():
        if i.endswith(a):
            with Image.open(i) as img:
                img2 = img.filter(ImageFilter.CONTOUR)
            img2.save('new2/' + str(i))

def z3():
    sum = 0
    with open("spisok.csv", "r") as file:
        read = csv.reader(file)
        next(read)
        for i in read:
            product = i[0]
            quantity = int(i[1])
            price = int(i[2])
            print(f"{product} - {quantity} шт. за {price} руб.")
            sum += quantity * price
    print(f"Итоговая сумма: {sum} руб.")


