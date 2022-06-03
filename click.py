from tkinter import *
from PIL import Image, ImageTk

nb_click = 0
multi_click = 1
auto_click = 0

click = [1, 50, 1000, 50000]
auto = [1, 50, 1000, 50000]
prix_click = [50, 1000, 20000, 500000]
prix_auto = [500, 5000, 120000, 5000000]

def clicks():
    global nb_click
    nb_click = nb_click + int(multi_click)
    canvas.delete('score')
    truc = refac(nb_click)
    canvas.create_text(500, 25, text='rainbow {}'.format(truc), fill='white', font=('Times', '16', 'bold'), tags='score')


def multi(y):
    global multi_click, click, prix_click, nb_click
    if 80<y<140:
        if prix_click[0] <= nb_click:
            nb_click = nb_click - prix_click[0]
            multi_click = int(click[0]) + multi_click
            click[0] = click[0]*1.25
            prix_click[0] = prix_click[0]*1.5
            canvas.delete('click1')
            canvas.delete('score')
            n1 = refac(click[0])
            n2 = refac((prix_click[0]))
            truc = refac(nb_click)
            canvas.create_text(100, 100, text='Plus {} par clic'.format(n1), fill='white', font=('Times', '18', 'bold'),
                               tags='click1')
            canvas.create_text(100, 120, text='Prix : {} rainbow'.format(n2), fill='white', font=('Times', '16', 'bold'),
                               tags='click1')
            canvas.create_text(500, 25, text='rainbow {}'.format(truc), fill='white', font=('Times', '16', 'bold'),
                              tags='score')

    if 180<y<240:
        if prix_click[1] <= nb_click:
            nb_click = nb_click - prix_click[1]
            multi_click = int(click[1]) + multi_click
            click[1] = click[1] * 1.25
            prix_click[1] = prix_click[1] * 1.5
            canvas.delete('click2')
            canvas.delete('score')
            n1 = refac(click[1])
            n2 = refac((prix_click[1]))
            truc = refac(nb_click)
            canvas.create_text(100, 200, text='Plus {} par clic'.format(n1), fill='white', font=('Times', '18', 'bold'),
                               tags='click2')
            canvas.create_text(100, 220, text='Prix : {} rainbow'.format(n2), fill='white',
                               font=('Times', '16', 'bold'),
                               tags='click2')
            canvas.create_text(500, 25, text='rainbow {}'.format(truc), fill='white', font=('Times', '16', 'bold'),
                               tags='score')

    if 280<y<340:
        if prix_click[2] <= nb_click:
            nb_click = nb_click - prix_click[2]
            multi_click = int(click[2]) + multi_click
            click[2] = click[2] * 1.25
            prix_click[2] = prix_click[2] * 1.5
            canvas.delete('click3')
            canvas.delete('score')
            n1 = refac(click[2])
            n2 = refac((prix_click[2]))
            truc = refac(nb_click)
            canvas.create_text(100, 300, text='Plus {} par clic'.format(n1), fill='white', font=('Times', '18', 'bold'),
                               tags='click3')
            canvas.create_text(100, 320, text='Prix : {} rainbow'.format(n2), fill='white',
                               font=('Times', '16', 'bold'),
                               tags='click3')
            canvas.create_text(500, 25, text='rainbow {}'.format(truc), fill='white', font=('Times', '16', 'bold'),
                               tags='score')

    if 380<y<440:
        if prix_click[3] <= nb_click:
            nb_click = nb_click - prix_click[3]
            multi_click = int(click[3]) + multi_click
            click[3] = click[3] * 1.25
            prix_click[3] = prix_click[3] * 1.5
            canvas.delete('click4')
            canvas.delete('score')
            n1 = refac(click[3])
            n2 = refac((prix_click[3]))
            truc = refac(nb_click)
            canvas.create_text(100, 400, text='Plus {} par clic'.format(n1), fill='white', font=('Times', '18', 'bold'),
                               tags='click4')
            canvas.create_text(100, 1420, text='Prix : {} rainbow'.format(n2), fill='white',
                               font=('Times', '16', 'bold'),
                               tags='click4')
            canvas.create_text(500, 25, text='rainbow {}'.format(truc), fill='white', font=('Times', '16', 'bold'),
                               tags='score')


def addauto(y):
    global auto_click, auto, prix_auto, nb_click

    if 80 < y < 140:
        if prix_auto[0] < nb_click:
            nb_click = nb_click - prix_auto[0]
            auto_click = int(auto[0]) + auto_click
            auto[0] = auto[0] * 1.25
            prix_auto[0] = prix_auto[0] * 1.5
            canvas.delete('auto1')
            canvas.delete('score')
            canvas.delete('score')
            n1 = refac(auto[0])
            n2 = refac((auto_click[0]))
            truc = refac(nb_click)
            canvas.create_text(900, 400, text='Plus {} par auto'.format(n1), fill='white', font=('Times', '18', 'bold'),
                               tags='auto1')
            canvas.create_text(900, 420, text='Prix : {} rainbow'.format(n2), fill='white',
                               font=('Times', '16', 'bold'),
                               tags='auto1')
            canvas.create_rectangle(805, 380, 996, 440, outline='white', width=3)

            canvas.create_text(500, 25, text='rainbow {}'.format(truc), fill='white', font=('Times', '16', 'bold'),
                               tags='score')

    if 180 < y < 240:
        if prix_auto[1] < nb_click:
            nb_click = nb_click - prix_auto[1]
            auto_click = int(auto[1]) + auto_click
            auto[1] = auto[1] * 1.25
            prix_auto[1] = prix_auto[1] * 1.5
            canvas.delete('auto2')
            canvas.delete('score')
            canvas.delete('score')
            n1 = refac(auto[1])
            n2 = refac((auto_click[1]))
            truc = refac(nb_click)
            canvas.create_text(900, 400, text='Plus {} par auto'.format(n1), fill='white', font=('Times', '18', 'bold'),
                               tags='auto2')
            canvas.create_text(900, 420, text='Prix : {} rainbow'.format(n2), fill='white',
                               font=('Times', '16', 'bold'),
                               tags='auto2')
            canvas.create_rectangle(805, 380, 996, 440, outline='white', width=3)

            canvas.create_text(500, 25, text='rainbow {}'.format(truc), fill='white', font=('Times', '16', 'bold'),
                               tags='score')

    if 280 < y < 340:
        if prix_auto[2] < nb_click:
            nb_click = nb_click - prix_auto[2]
            auto_click = int(auto[2]) + auto_click
            auto[2] = auto[3] * 1.25
            prix_auto[2] = prix_auto[2] * 1.5
            canvas.delete('auto3')
            canvas.delete('score')
            n1 = refac(auto[2])
            n2 = refac((auto_click[2]))
            truc = refac(nb_click)
            canvas.create_text(900, 400, text='Plus {} par auto'.format(n1), fill='white', font=('Times', '18', 'bold'),
                               tags='auto3')
            canvas.create_text(900, 420, text='Prix : {} rainbow'.format(n2), fill='white',
                               font=('Times', '16', 'bold'),
                               tags='auto3')
            canvas.create_rectangle(805, 380, 996, 440, outline='white', width=3)

            canvas.create_text(500, 25, text='rainbow {}'.format(truc), fill='white', font=('Times', '16', 'bold'),
                               tags='score')


    if 380<y<440:
        if prix_auto[3] < nb_click:
            nb_click = nb_click - prix_auto[3]
            auto_click = int(auto[3]) + auto_click
            auto[3] = auto[3] * 1.25
            prix_auto[3] = prix_auto[3] * 1.5
            canvas.delete('auto4')
            canvas.delete('score')
            canvas.delete('score')
            n1 = refac(auto[3])
            n2 = refac((auto_click[3]))
            truc = refac(nb_click)
            canvas.create_text(900, 400, text='Plus {} par auto'.format(n1), fill='white', font=('Times', '18', 'bold'),
                               tags='auto4')
            canvas.create_text(900, 420, text='Prix : {} rainbow'.format(n2), fill='white', font=('Times', '16', 'bold'),
                               tags='auto4')
            canvas.create_rectangle(805, 380, 996, 440, outline='white', width=3)

            canvas.create_text(500, 25, text='rainbow {}'.format(truc), fill='white', font=('Times', '16', 'bold'),
                               tags='score')


def clic(event):
    x = event.x
    y = event.y

    if 375<x<625 and 160<y<405:
        clicks()

    if 5<x<200:
        multi(y)

    if 805<x<996:
        addauto(y)


def refac(num):
    if 999<num<999999:
        save = int(num/1000)
        save = '{}K'.format(save)
        return save
    if 999999<num<999999999:
        save = int(num/1000000)
        save = '{}M'.format(save)
        return save
    if 999999999<num<999999999999:
        save = int(num/1000000000)
        save = '{}B'.format(save)
        return save
    if 999999999999<num<99999999999999:
        save = int(num/1000000000000)
        save = '{}T'.format(save)
        return save
    return int(num)


def runauto():
    global nb_click
    nb_click = nb_click + auto_click
    canvas.delete('score')
    truc = refac(nb_click)
    canvas.create_text(500, 25, text='rainbow {}'.format(truc), fill='white', font=('Times', '16', 'bold'),
                       tags='score')
    root.after(1000, runauto)

root = Tk()
root.title("Game")

canvas = Canvas(root, bg="black", width=1000, height=562)
canvas.pack()

canvas.bind('<Button-1>', clic)

img = (Image.open("chatarc.png"))
resized_image = img.resize((250, 250), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
image = Image.open("arc.jpg")
photo = ImageTk.PhotoImage(image)
item4 = canvas.create_image(500, 281, image=photo)
canvas.create_image(500, 281, image=new_image)

canvas.create_text(100,100, text='Plus 1 par clic', fill='white', font=('Times', '18', 'bold'), tags='click1')
canvas.create_text(100,120, text='Prix : 50 rainbow', fill='white', font=('Times', '16', 'bold'), tags='click1')
canvas.create_rectangle(5, 80, 196, 140, outline='white', width=3)

canvas.create_text(100,200, text='Plus 50 par clic', fill='white', font=('Times', '18', 'bold'), tags='click2')
canvas.create_text(100,220, text='Prix : 1K rainbow', fill='white', font=('Times', '16', 'bold'), tags='click2')
canvas.create_rectangle(5, 180, 196, 240, outline='white', width=3)

canvas.create_text(100,300, text='Plus 1K par clic', fill='white', font=('Times', '18', 'bold'), tags='click3')
canvas.create_text(100,320, text='Prix : 20K rainbow', fill='white', font=('Times', '16', 'bold'), tags='click3')
canvas.create_rectangle(10, 280, 196, 340, outline='white', width=3)

canvas.create_text(100,400, text='Plus 50K par clic', fill='white', font=('Times', '18', 'bold'), tags='click4')
canvas.create_text(100,420, text='Prix : 500K rainbow', fill='white', font=('Times', '16', 'bold'), tags='click4')
canvas.create_rectangle(10, 380, 196, 440, outline='white', width=3)

canvas.create_text(900,100, text='Plus 1 par auto', fill='white', font=('Times', '18', 'bold'), tags='auto1')
canvas.create_text(900,120, text='Prix : 500 rainbow', fill='white', font=('Times', '16', 'bold'), tags='auto1')
canvas.create_rectangle(805, 80, 996, 140, outline='white', width=3)

canvas.create_text(900,200, text='Plus 50 par auto', fill='white', font=('Times', '18', 'bold'), tags='auto2')
canvas.create_text(900,220, text='Prix : 5K rainbow', fill='white', font=('Times', '16', 'bold'), tags='auto2')
canvas.create_rectangle(805, 180, 996, 240, outline='white', width=3)

canvas.create_text(900,300, text='Plus 1K par auto', fill='white', font=('Times', '18', 'bold'), tags='auto3')
canvas.create_text(900,320, text='Prix : 120K rainbow', fill='white', font=('Times', '16', 'bold'), tags='auto3')
canvas.create_rectangle(805, 280, 996, 340, outline='white', width=3)

canvas.create_text(900,400, text='Plus 50K par auto', fill='white', font=('Times', '18', 'bold'), tags='auto4')
canvas.create_text(900,420, text='Prix : 5M rainbow', fill='white', font=('Times', '16', 'bold'), tags='auto4')
canvas.create_rectangle(805, 380, 996, 440, outline='white', width=3)

canvas.create_text(500, 25, text='rainbow 0', fill='white', font=('Times', '16', 'bold'), tags='score')


runauto()

root.mainloop()
