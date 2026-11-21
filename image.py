from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class WMImage():
    def __init__(self, parent):
        self.label = ttk.Label(parent, text="No file selected")
        self.img = PhotoImage()
        self.display = ttk.Label(parent, image=self.img)
        self.loc = StringVar()
        self.loc.trace_add("write", callback=self.getImage)

    def grid(self, row=0, column=0):
        self.display.grid(column=column, row=row)
        self.label.grid(column=column, row=row + 5)

    def getImage(self, *args):
        imgobj = ImageTk.PhotoImage(Image.open(self.label.getvar(args[0])))
        self.display.configure(image=imgobj)
        self.display.image = imgobj