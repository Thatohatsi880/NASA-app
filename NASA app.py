import tkinter as tk
from tkinter import ttk
from tkinter import *
import PIL
from PIL import imageTK, PILImage

GREEN = '#8dc24e'

HEIGHT = 700
WIDTH = 900

root = tk.Tk()
root.title('Welcome to my planet app')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#171717')
canvas.pack()
mainloop()
