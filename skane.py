from tkinter import *
import serial
import random
from time import sleep

ser = serial.Serial('COM10', 9600)

width = 32
height = 8

lum = 0
pix = 0
mat = [[1 for i in range(width)] for j in range(height)]


squareSize = 45
oldsnake = [[0,0],[0,1],[0,2],[0,3]]
oldsnake2 = [[0,0],[0,0],[0,1],[0,2]]
snake = [[0,0],[0,1],[0,2],[0,3]]
pomme = [0, 0]
DIR = {'Left': (-1, 0), 'Right': (1, 0), 'Up': (0, -1), 'Down': (0, 1)}
x, y = 0, 0
direction = [1, 0]


def mvt_event(event):
    global direction
    key = event.keysym
    dx, dy = DIR[key]
    direction = [dx, dy]


def linecreate():
    for i in range(width):
        can.create_line(squareSize * i, 0, squareSize * i, squareSize * height, fill='white', width=1, tags='rect')

    for i in range(height):
        can.create_line(0, squareSize * i, squareSize * width, squareSize * i, fill='white', width=1,tags='rect')


def pommecreate():
    global pomme
    can.delete("pomme")
    pomme = [random.randint(0, 31), random.randint(0, 7)]
    can.create_rectangle(squareSize * pomme[0], squareSize * pomme[1], (pomme[0] + 1) * squareSize,
                         (pomme[1] + 1) * squareSize, fill="red", tags="pomme")


def snakecreate():
    global snake
    can.delete("snake")
    for i in snake:
        can.create_rectangle(squareSize * i[0], squareSize * i[1], (i[0] + 1) * squareSize,
                             (i[1] + 1) * squareSize, fill="#00ff00", tags="snake")


def amange():
    global snake
    if snake[-1][0] == pomme[0] and snake[-1][1] == pomme[1]:
        can.create_rectangle(squareSize * pomme[0], squareSize * pomme[1], (pomme[0] + 1) * squareSize,
                             (pomme[1] + 1) * squareSize, fill="#00ff00", tags="snake")
        snake.append(pomme)
        return 1
    return 0


def depsnake():
    global snake
    oldsnake = []
    for i in range(len(snake) - 1):
        oldsnake.append(snake[i+1])

    for i in range(len(snake) - 1):
        snake[i] = oldsnake[i]
    tete = [oldsnake[-1][0] + direction[0], oldsnake[-1][1] + direction[1]]
    snake[-1]=(tete)



def reset():
    global snake, direction
    snake = [[0, 0], [0, 1], [0, 2], [0, 3]]
    direction = [1, 0]
    sleep(5)



def collision():
    for i in range(len(snake)-2):
        if snake[i][0]==32 or snake[i][0]==-1:
            print("gameover")
            reset()
        if snake[i][1]==8 or snake[i][1]==-1:
            print("gameover")
            reset()


def affichage():
    setpix = '{}{}'.format(2, 000)
    ser.write(bytes(setpix, 'utf-8'))
    lum = 0
    sleep(0.01)
    if (pomme[0] % 2) == 0:
        pix = pomme[0] * 8 + pomme[1]
    else:
        pix = pomme[0] * 8 + (8 - pomme[1]) - 1

    setpix = '{}{}'.format(lum, pix)
    print(setpix)
    ser.write(bytes(setpix, 'utf-8'))
    sleep(0.01)

    for i in snake:
        lum = 1
        sleep(0.01)
        if (i[0] % 2) == 0:
            pix = i[0] * 8 + i[1]
        else:
            pix = i[0] * 8 + (8 - i[1]) - 1
        setpix = '{}{}'.format(lum, pix)

        ser.write(bytes(setpix, 'utf-8'))


def main():
    depsnake()
    if amange()==1:
        pommecreate()
    snakecreate()
    affichage()
    time=250-len(snake)*3
    collision()
    rt.after(time, main)




rt = Tk()

for key in ["<Left>", "<Right>", "<Up>", "<Down>"]:
    rt.bind(key, mvt_event)

can = Canvas(rt, width=(width)* squareSize, height=(height)* squareSize, bg='#000000')
can.pack()
linecreate()
Button (rt, text='rejouer', command=reset).pack()
pommecreate()
snakecreate()
main()

rt.mainloop()


