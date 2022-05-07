import tkinter as tk
from tkinter import ttk
from tkinter import *
import PIL
from PIL import imageTK, PILImage

GRAY = '#808080'

HEIGHT = 700
WIDTH = 900

root = tk.Tk()
root.title('Welcome to my fun planet app')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#800080')
canvas.pack()

desc_frame = tk.Frame(root, bg='#0000FF')
desc_frame.place(relx=0.6, rely=0.1, relheight=0.6, relwidth=0.35)

fact_frame = tk.Frame(root, bg='#0000FF')
fact_frame.place((relx=0.06, rely=0.72, relheight=0.2, relwidth=0.9)
                 
option = ["Uranus", "Neptune", "Jupiter", "Earth", "Stars", "Venus", "Saturn", "Mercury", "Mars", "Pluto"]
clicked = StringVar()
clicked.set(option(0))
drop = OptionMenu(root, clicked, option)
drop.config(bg ='#0000FF', fg = Gray)

mainloop()
