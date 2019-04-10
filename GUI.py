
import matplotlib.figure as mpl
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import *
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.backends.tkagg as tkagg

def sel():
   selection = "You selected the option " + var.get()
   #label.config(text = selection)
   type_str = var.get()
   print(type_str)

def getTemp():
	with open(type_str	, 'r') as f:
		data = f.readlines()
	data[1] = TempEntry.get() + '\n'
	with open(type_str,'w') as f:
		f.writelines(data)
		
def draw_figure(canvas, figure, loc=(0, 0)):
    """ Draw a matplotlib figure onto a Tk canvas

    loc: location of top-left corner of figure on canvas in pixels.
    Inspired by matplotlib source: lib/matplotlib/backends/backend_tkagg.py
    """
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)

    # Position: convert from top-left anchor to center anchor
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)

    # Unfortunately, there's no accessor for the pointer to the native renderer
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)

    # Return a handle which contains a reference to the photo object
    # which must be kept live or else the picture disappears
    return photo

root = Tk()
root.title('Pulsar GUI')
root.geometry('500x500')

rows = 0
while rows < 50:
	root.rowconfigure(rows, weight=1)
	root.columnconfigure(rows, weight=1)
	rows += 1

n = ttk.Notebook(root)
n.grid(row=1, column=1, columnspan=50, rowspan=49, sticky='NESW')
f1 = ttk.Frame(n) #first page
f2 = Canvas(n) #second page
n.add(f1, text = 'Input Tab')
n.add(f2, text = 'Output Tab')
n.select(f1)
n.enable_traversal()

var = StringVar()
var.set("L")
R1 = Radiobutton(f1, text="Cepheid", variable=var, value="CepheidFile.txt", command=sel)
R1.pack( anchor = W )
R2 = Radiobutton(f1, text="RR-Lyrae", variable=var, value="RRLyraeFile.txt", command=sel)
R2.pack( anchor = W )


MassLabel = Label(f1, text = "Mass")
MassLabel.pack(anchor = W)
MassEntry = Entry(f1, bd = 15)
MassEntry.pack(anchor = W)

TempLabel = Label(f1, text = "Temperature")
TempLabel.pack(anchor = W)
TempEntry = Entry(f1, bd = 15)
TempEntry.pack(anchor = W)

LumLabel = Label(f1, text = "Luminosity")
LumLabel.pack(anchor = W)
LumEntry = Entry(f1, bd = 15)
LumEntry.pack(anchor = W)

XLabel = Label(f1, text = "Hydrogen Composition")
XLabel.pack(anchor = W)
XEntry = Entry(f1, bd = 15)
XEntry.pack(anchor = W)

ZLabel = Label(f1, text = "Metal Composition")
ZLabel.pack(anchor = W)
ZEntry = Entry(f1, bd = 15)
ZEntry.pack(anchor = W)

MaxPeriodLabel = Label(f1, text = "Max Period")
MaxPeriodLabel.pack(anchor = W)
MaxPeriodEntry = Entry(f1, bd = 15)
MaxPeriodEntry.pack(anchor = W)

MaxAmpLabel = Label(f1, text = "Max Amp")
MaxAmpLabel.pack(anchor = W)
MaxAmpEntry = Entry(f1, bd = 15)
MaxAmpEntry.pack(anchor = W)

ProgressBar = Text(f1, height = 1, width = 50)
ProgressBar.pack(side = LEFT)
quote = "Something is happening"
ProgressBar.insert(END, quote)

submit = Button(f1, text = "Submit", command = getTemp)
submit.pack(side = BOTTOM)


X = np.linspace(0, 2 * np.pi, 50)
Y = np.sin(X)

fig = mpl.Figure(figsize=(2, 1))
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(X, Y)

fig_x, fig_y = 100, 100
fig_photo = draw_figure(f2, fig, loc=(fig_x, fig_y))
fig_w, fig_h = fig_photo.width(), fig_photo.height()

root.mainloop()