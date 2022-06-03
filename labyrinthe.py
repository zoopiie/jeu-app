from tkinter import *

lab1 =[[0,0,0,0,1,0],
               [0,0,1,0,1,0],
               [1,1,1,0,1,0],
               [1,0,0,0,0,0],
               [1,1,1,0,1,1],
               [0,0,0,0,0,0]]


lab2 = [[0,0,0,0,1,0,0,0,1,1,0,1],
        [1,1,1,0,1,0,1,0,0,0,0,1],
        [1,1,1,0,1,1,1,0,1,1,0,1],
        [0,0,0,0,1,0,1,1,0,1,0,1],
        [0,1,1,1,1,0,1,0,0,1,0,1],
        [0,1,1,0,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,0,1,0,1,1,0,1],
        [0,0,1,0,1,0,1,0,1,1,0,1],
        [0,0,1,0,0,1,1,1,1,0,0,0],
        [0,1,0,0,0,0,0,0,1,0,1,0],
        [0,0,1,1,1,1,0,1,1,0,1,1],
        [0,0,0,0,0,0,0,0,1,0,0,0]]

lab3 =[[0,1,1,1,1,1,1,1,1,0,0,1,0,0,1],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [0,1,0,1,1,1,1,0,1,1,1,1,1,0,1],
       [0,1,0,1,0,0,1,0,1,0,0,0,0,0,1],
       [0,1,0,1,0,0,1,0,1,1,1,1,1,0,1],
       [0,1,0,1,0,1,1,0,1,0,0,0,0,0,1],
       [0,1,0,1,0,1,1,0,1,0,0,0,0,1,1],
       [0,1,0,1,0,1,1,0,1,0,1,1,0,0,0],
       [1,1,0,1,0,0,1,0,1,0,0,1,0,0,0],
       [0,1,0,1,1,0,1,0,1,0,1,1,1,1,0],
       [0,1,0,1,0,0,1,0,1,0,0,0,0,1,0],
       [0,1,0,1,0,1,1,0,1,0,1,1,1,1,0],
       [0,1,0,1,0,0,0,0,1,0,0,0,0,0,1],
       [0,1,1,1,1,1,1,1,1,1,1,0,1,1,1],
       [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]]

def labcreate(lab):
    n = len(lab)
    print(n)

    for i in range(n+1):
        for j in range(n+1):
            a = (i ) * 50
            b = (i+1) * 50
            aa = (j ) * 50
            bb = (j+1) * 50

            bg = lab[i - 1][j - 1]
            if (bg == 1):
                can.create_rectangle(a, aa, b, bb, fill='black')
            else:
                can.create_rectangle(a, aa, b, bb, fill='#00eeee')

    n = len(lab)+1
    can.create_rectangle(50 * (n - 1), 50 * (n - 1), 50 * n, 50 * n, fill='red')

    for i in range(n):
        can.create_line(50 * i, 0, 50 * i, 50 * n, fill='white', width=1)

    for i in range(n):
        can.create_line(0, 50 * i, 50 * n, 50 * i, fill='white', width=1)

    can.create_rectangle(0, 0, 50, 50, fill='#ff7801')

DIR={'Left':(-1,0),'Right':(1,0),'Up':(0,-1),'Down':(0,1)}

x ,y= 0 ,0

def mvt(event):
    global x,y
    key = event.keysym
    dx, dy = DIR[key]
    xx = dx + x
    yy = dy + y
    if (yy==15 and xx==15):
        can.delete()
        label = Label(rt, text=' victoire !!! ', font=('Courrier',34), fg='purple').pack()
    if (lab3[xx - 1][yy - 1] == 0):
        if (0<=yy<(len(lab3)+1) and 0<=xx<(len(lab3)+1)):
            x = dx + x
            y = dy + y

            print(x,y)
            can.create_rectangle(x*50,y*50, (x+1)*50, (y+1)*50, fill='#ff7801')
            can.create_rectangle((x-dx)*50,(y-dy)*50, (x+1-dx)*50, (y+1-dy)*50, fill='#00eeee')


        
    
        
    





rt = Tk()

n=len(lab3)

can = Canvas(rt, width=(n+1 )* 50, height=(n+1) * 50)
can.pack()

labcreate(lab3)



for key in ["<Left>", "<Right>", "<Up>", "<Down>"]:
    rt.bind(key, mvt)

rt.mainloop()