import tkinter as tk


win = tk.Tk()
win.config(bg="red")

canvas = tk.Canvas(win, width=200, height=200)
canvas.create_rectangle(0,0,66,66, fill="orange")
canvas.pack()


img = tk.PhotoImage(file='pngegg.png')


canvas.create_image(10,10, image=img)

canvas.create_text(10,10, text="This isn't ideal but it works", anchor="nw", font=(55))
win.mainloop()