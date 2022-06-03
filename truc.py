from tkinter import *
from PIL import Image, ImageOps


root = Tk()
root.title("Game")


frame = Frame(root)
frame.pack()


canvas = Canvas(frame, bg="black", width=700, height=400)
canvas.pack()


background = PhotoImage(file="soleil.png")
canvas.create_image(350,200,image=background)

character = PhotoImage(file="pngegg.png")
canvas.create_image(30,30,image=character)

root.mainloop()


im = im.rotate(45)

im_mirror = ImageOps.mirror(im)

im_flip = ImageOps.flip(im)