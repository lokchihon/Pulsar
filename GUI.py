import tkinter
from tkinter import ttk
from tkinter import *

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
f2 = ttk.Frame(n) #second page
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
R3 = Radiobutton(f1, text="Common", variable=var, value="myfile.txt", command=sel)
R3.pack( anchor = W)

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

submit = Button(f1, text = "Submit", command = getTemp)
submit.pack(side = RIGHT)

root.mainloop()
