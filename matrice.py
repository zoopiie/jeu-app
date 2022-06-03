from tkinter import *
from PIL import Image, ImageTk

x = 0
def plus():
    global x
    x = x*x+1
    mon_compteur.config(text=x)

root = Tk()
root.geometry('800x400')
root.title('dklhnjaq')

image = Image.open("caillou.jpg")
resize_image = image.resize((800, 400))
img = ImageTk.PhotoImage(resize_image)

label1 = Label(image=img)
label1.image = img
label1.place(x=0, y=0)

image2 =Image.open('cookie.jpg')
resize_image2 = image2.resize((120, 100))
img2 = ImageTk.PhotoImage(resize_image2)

but = Button(image=img2, command=plus)
but.image = img
but.place(x=300, y=100)

mon_texte = Label(root, text=" Nombre de click", font=(30), fg='blue', bg='white')
mon_texte.place(x=300, y=300)
mon_compteur = Label(root, text=x, font=(30), fg='black', bg='white')
mon_compteur.place(x=320, y=320)

root.mainloop()