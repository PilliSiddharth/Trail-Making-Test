from tkinter import *
import io
import urllib.request
from PIL import ImageTk, Image


def get_x_and_y(event):
  global lasx, lasy
  lasx, lasy = event.x, event.y
  print("Pointer is currently at %d, %d" % (lasx, lasy))


def draw_smth(event):
  global lasx, lasy
  wn.create_line((lasx, lasy, event.x, event.y),
                     fill='red',
                     width=2)
  lasx, lasy = event.x, event.y

canvas = Tk()
background = Image.open("TMT-B.jpg")
width, height = background.size
background = background.resize((width // 2, height // 2))
tkimage = ImageTk.PhotoImage(background)
# panel1 = Label(canvas, image=tkimage)
# panel1.grid(ipadx=0, ipady=0, sticky=E)


wn =Canvas(canvas, bg="white", width=600, height=600)
wn.pack(anchor="nw", fill="both", expand=1)
# wn.create_text(panel1)
wn.create_image(0,0, image=tkimage, anchor="nw")



canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw_smth)
# canvas.pack()

canvas.resizable(False, False)
mainloop()