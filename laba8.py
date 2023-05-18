from PIL import Image, ImageDraw, ImageFont

def z1():
    otkritka = Image.open('spasibo0037.jpg')
    otkritka_crop = otkritka.crop((300, 150, 1000, 500))
    otkritka_crop.save("123.jpg")
    otkritka_crop.show()

def z2():
    prazdnik = {
        "День победы" : "may.jpg",
        "8 марта" : "mart.jpg",
        "День рождения" : "dr.jpg"
    }
    otkritka = input("Какой сейчас празник?:   ")
    if otkritka in prazdnik:
        image = Image.open(prazdnik[otkritka])
        image.show()
    else:
        print("такой открытки нет")

def z3():
    name = input("Введите получателя:  ")
    filename = "dr.jpg"
    with Image.open(filename) as img:
        img.load()
    font = ImageFont.truetype("arial.ttf", 30)
    draw = ImageDraw.Draw(img)
    draw.text((img.width // 2 - 100, 15), name + ' ,поздавляю!', font=font, fill=('red'))
    img.show()
    img.save(name + "dr2.png")
