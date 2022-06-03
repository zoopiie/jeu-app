from tkinter import *
import serial

ser = serial.Serial('COM10', 9600)

l = 32

h = 8
lum = 0
pix = 0
mat = [[1 for i in range(l)] for j in range(h)]

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



                if (mat[j][i]==0):
                    can.create_rectangle(50*i,50*j,(i+1)*50,(j+1)*50, fill='#00eeee', tags='rect')
                    lum = 1
                    mat[j][i] = 1

                else:
                    can.create_rectangle(50*i,50*j,(i+1)*50,(j+1)*50, fill='black', tags='rect')
                    lum = 0
                    mat[j][i] = 0

    setpix = '{}{}'.format(lum, pix)
    ser.write(bytes(setpix, 'utf-8'))



def reset():
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
    mat = [[0 for i in range(l)] for j in range(h)]


rt = Tk()

can = Canvas(rt, width=(l)* 50, height=(h)* 50, bg='#00eeee')
can.pack()
linecreate()
Button (rt, text='reset led matrix', command=reset).pack()
Button (rt, text='etiendre led matrix', command=noir).pack()
can.bind('<Button-1>', clic)

rt.mainloop()


