from tkinter import *
import random
from time import sleep
from threading import Timer
import keyboard

width = int(input('nombre de carré en largueur :'))

height = int(input('nombre de carré en hauteur :'))

matrix = [[1 for i in range(width)] for j in range(height)]
matrixBis = [[0 for i in range(width)] for j in range(height)]

squareSize = 30
stopvar = 1
bonus = 0
DIR = {'Left': (-1, 0), 'Right': (1, 0), 'Up': (0, -1), 'Down': (0, 1)}
x, y = 0, 0

def build_color_string(prefix, suffix, randomcolor):
    hex_value = hex(randomcolor)[2::]  # On deleterime le préfixe '0x' de la chaine hexadecimal
    if randomcolor < 16:
        add_char = "0"
        hex_value = "%s%s" % (add_char, hex_value)
    hexcolor = "%s%s%s" % (prefix, hex_value, suffix)
    return hexcolor



def hex_color():
    # 16 x 16 = 256
    # 256 x 6 = 1536 (6 unités dans un hexadécimal #F1A456)
    # 1536 + 4 = 1540 (4 teintes de blanc)
    randomcolor = random.randint(0, 1540)

    if 0 <= randomcolor <= 255:
        hexcolor = build_color_string("#ff", "00", randomcolor)

    if 256 <= randomcolor <= 511:
        randomcolor = 511 - randomcolor
        hexcolor = build_color_string("#", "ff00", randomcolor)

    if 512 <= randomcolor <= 767:
        randomcolor = randomcolor - 512
        hexcolor = build_color_string("#ff00", "", randomcolor)

    if 768 <= randomcolor <= 1023:
        randomcolor = 1023 - randomcolor
        hexcolor = build_color_string("#00", "ff", randomcolor)

    if 1024 <= randomcolor <= 1279:
        randomcolor = randomcolor - 1024
        hexcolor = build_color_string("#", "00ff", randomcolor)

    if 1278 <= randomcolor <= 1535:
        randomcolor = 1535 - randomcolor
        hexcolor = build_color_string("#ff00", "", randomcolor)

    if 1536 <= randomcolor:
        hexcolor = "#ffffff"

    return hexcolor


def color():
    global matrix, stopvar
    colorfill = hex_color()

    j = random.randint(0, width - 1)
    i = random.randint(0, height - 1)

    if matrix[i][j] == 0:
        can.create_rectangle(squareSize * j, squareSize * i, (j + 1) * squareSize, (i + 1) * squareSize, fill=colorfill)
        if matrix == matrixBis:
            print('fullcolor')
            clean_all()

    else:
        can.create_rectangle(squareSize * j, squareSize * i, (j + 1) * squareSize, (i + 1) * squareSize, fill=colorfill)
        matrix[i][j] = 0
    if stopvar == 1:
        Timer(0.00001, color).start()


def clean_all():
    global matrix
    matrix = [[1 for i in range(width)] for j in range(height)]
    can.create_rectangle(0, 0, squareSize * width, squareSize * height, fill='black')


def stop():
    global stopvar, x, y
    stopvar = 1 - stopvar
    x, y = 0, 0

    if stopvar == 1:
        color()


def cheat():
    global bonus
    bonus = 1 - bonus


def mvt_event(event):
    global x, y, bonus, matrix
    key = event.keysym
    dx, dy = DIR[key]
    xx = dx + x
    yy = dy + y
    if yy == width - 1 and xx == height - 1:
        can.delete()
        label = Label(rt, text=' victoire !!! ', font=('CousquareSizeier', 34), fg='purple').pack()
    if bonus == 0:
        if xx < width and yy < height:
            if matrix[yy][xx] == 1:
                if 0 <= yy < (len(matrix)) and 0 <= xx < (len(matrix[0])):
                    x = dx + x
                    y = dy + y

                    can.create_rectangle(x * squareSize, y * squareSize, (x + 1) * squareSize, (y + 1) * squareSize,
                                         fill='#00ffe0')
                    can.create_rectangle((x - dx) * squareSize, (y - dy) * squareSize, (x + 1 - dx) * squareSize,
                                         (y + 1 - dy) * squareSize, fill='black')
    if bonus == 1:
        if 0 <= yy < (len(matrix)) and 0 <= xx < (len(matrix[0])):
            x = dx + x
            y = dy + y
            matrix[yy][xx] == 1

            can.create_rectangle(x * squareSize, y * squareSize, (x + 1) * squareSize, (y + 1) * squareSize,
                                 fill='#00ffe0')
            can.create_rectangle((x - dx) * squareSize, (y - dy) * squareSize, (x + 1 - dx) * squareSize,
                                 (y + 1 - dy) * squareSize, fill='grey')


def boom():
    global x, y, matrix
    if 1 < x < width - 2 and 1 < y < height - 2:
        for i in range(5):
            for j in range(5):
                can.create_rectangle((x - 2 + i) * squareSize, (y - 2 + j) * squareSize, (x - 2 + i + 1) * squareSize,
                                     (y - 2 + j + 1) * squareSize,
                                     fill='grey')
                matrix[y - 2 + j][x - 2 + i] = 1

    can.create_rectangle(x * squareSize, y * squareSize, (x + 1) * squareSize, (y + 1) * squareSize, fill='#00ffe0')


def delete(i, j):
    global matrix
    print(type(i), i, type(j), j)
    sleep(0.0001)
    if i < height and j < width:
        can.create_rectangle(j * squareSize, i * squareSize, (j + 1) * squareSize, (i + 1) * squareSize,
                             fill='grey')
        i = i + 1
        Timer(0.005, delete, args=(i, j)).start()
    if i == height - 1 and j < width:
        can.create_rectangle(j * squareSize, i * squareSize, (j + 1) * squareSize, (i + 1) * squareSize,
                             fill='grey')
        i = 0
        j = j + 1
        Timer(0.005, delete, args=(i, j)).start()

    if j == width:
        print("hello")
        matrix = [[1 for i in range(width)] for j in range(height)]
        can.create_rectangle(0, 0, squareSize * width, squareSize * height, fill='grey')


rt = Tk()
rt.title('assis toi et admire')
rt.wm_attributes('-transparentcolor', 'grey')

for key in ["<Left>", "<Right>", "<Up>", "<Down>"]:
    rt.bind(key, mvt_event)

keyboard.on_press_key("space", lambda _: boom())

keyboard.on_press_key("enter", lambda _: cheat())

keyboard.on_press_key("ctrl", lambda _: stop())

keyboard.on_press_key("delete", lambda _: delete(0, 0))

keyboard.on_press_key("0", lambda _: clean_all())

can = Canvas(rt, width=width * squareSize, height=height * squareSize, bg='black')
can.pack()
button = Button(rt, text='stop le bazar', command=stop).pack(side=LEFT)
button1 = Button(rt, text='le bonus qui fait plaisir', command=cheat).pack(side=LEFT)

color()

rt.mainloop()
