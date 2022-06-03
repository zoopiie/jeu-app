from tkinter import *
import serial

ser = serial.Serial('COM3', 9600)

rhex = "00"
bhex = "00"
ghex = "00"

red = "000"
blue = "000"
green = "000"

l = 32

h = 8
lum = 0
pix = 0
mat = [[[0 for g in range(4)] for i in range(l)] for j in range(h)]

old_x, old_y = 0, 0

def linecreate():
    for i in range(l):
        can.create_line(50 * i, 0, 50 * i, 50 * h, fill='white', width=1, tags='rect')

    for i in range(h):
        can.create_line(0, 50 * i, 50 * l, 50 * i, fill='white', width=1,tags='rect')



def clic(event):
    global old_x, old_y, mat, lum, pix

    old_x = event.x
    old_y = event.y




    for i in range(0,l):
        for j in range(0,h):
            if (i*50<old_x<(i+1)*50  and j*50<old_y<(j+1)*50 ):


                if (i % 2) == 0:
                    pix = i * 8 + j
                else:
                    pix = i * 8 + (8 - j) - 1



                if (mat[j][i][3]==0):
                    can.create_rectangle(50*i,50*j,(i+1)*50,(j+1)*50, fill='#{}{}{}'.format(rhex, ghex, bhex), tags='rect')
                    lum = 1
                    mat[j][i] = [int(var_rouge.get()), int(var_vert.get()), int(var_bleu.get()), 1]

                else:
                    can.create_rectangle(50*i,50*j,(i+1)*50,(j+1)*50, fill='black', tags='rect')
                    lum = 0
                    mat[j][i] = [0, 0, 0, 0]

    setpix = '{}{}{}{}{}'.format(lum, red, green, blue, pix)
    ser.write(bytes(setpix, 'utf-8'))



def blanc():
    global mat
    mat = [[1 for i in range(l)] for j in range(h)]
    setpix = '2000'
    linecreate()
    can.delete('rect')
    ser.write(bytes(setpix, 'utf-8'))

def noir():
    global mat
    setpix = '3000'
    can.delete('rect')
    can.create_rectangle(0, 0, 32 * 50, 400, fill='black', tags='rect')
    linecreate()
    ser.write(bytes(setpix, 'utf-8'))
    mat = [[[0 for g in range(4)] for i in range(l)] for j in range(h)]


def couleur():
    color = '#{}{}{}'.format(rhex, ghex, bhex)
    label.config(bg=color)

def couleurb(v):
    global bhex, blue
    blue = int(var_bleu.get())

    bhex = hex(blue)[2:]
    if int(blue)<16 :
        bhex = "0{}".format(bhex)
    if int(blue) < 10:
        blue = '00{}'.format(blue)
    if 10 <= int(blue) < 100:
        blue = '0{}'.format(blue)
    couleur()


def couleurr(v):
    global rhex, red
    red = int(var_rouge.get())
    rhex = hex(red)[2:]
    if int(red)<16 :
        rhex = "0{}".format(rhex)
    if int(red) < 10:
        red = '00{}'.format(red)
    if 10 <= int(red) < 100:
        red = '0{}'.format(red)
    couleur()

def couleurg(v):
    global ghex, green
    green = int(var_vert.get())
    ghex = hex(green)[2:]
    if int(green)<16 :
        ghex = "0{}".format(ghex)
    if int(green) < 10:
        green = '00{}'.format(green)
    if 10 <= int(green) < 100:
        green = '0{}'.format(green)
    couleur()

rt = Tk()

can = Canvas(rt, width=(l)* 50, height=(h)* 50, bg='black')
can.pack()
noir()
Button (rt, text='reset led matrix', command=noir).pack()
Button (rt, text='allumer led matrix', command=blanc).pack()
can.bind('<Button-1>', clic)

var_rouge = DoubleVar()
rouge = Scale(rt, orient='horizontal', from_=0, to=255,
      resolution=1, tickinterval=36, length=350,
      label='rouge', variable=var_rouge, command=couleurr)
rouge.pack(side=LEFT)

var_vert = DoubleVar()
vert = Scale(rt, orient='horizontal', from_=0, to=255,
      resolution=1, tickinterval=36, length=350,
      label='vert', variable=var_vert, command=couleurg)
vert.pack(side=LEFT)

var_bleu = DoubleVar()
bleu = Scale(rt, orient='horizontal', from_=0, to=255,
      resolution=1, tickinterval=36, length=350,
      label='bleu', variable=var_bleu, command=couleurb)
bleu.pack(side=LEFT)

label = Label(rt, text='                                 ', bg="white", font=80)
label.pack(side=LEFT)

rt.mainloop()
