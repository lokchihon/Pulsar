import matplotlib.figure as mpl
from Pulsar import Pulsar
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import *
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.backends.tkagg as tkagg
import re
import mesa_reader as mr
import matplotlib.pyplot as pl

def helper():
    r = re.compile("^[0-9]*(?:\.[0-9]{0,4})?$")
    if MassEntry.get() == "" or LumEntry.get() == "" or TempEntry.get() == "" or XEntry.get() == "" or ZEntry.get() == "" or MaxPeriodEntry.get() == "" or MaxAmpEntry.get() == "":
        ProgressBar.delete(1.0, END)
        ProgressBar.insert(END, "Variables cannot be left blank")
        return False
    if not (bool(r.match(MassEntry.get())) and bool(r.match(LumEntry.get())) and bool(r.match(TempEntry.get())) and
            bool(r.match(XEntry.get())) and bool(r.match(ZEntry.get())) and bool(r.match(MaxPeriodEntry.get())) and
            bool(r.match(MaxAmpEntry.get()))):
        ProgressBar.delete(1.0, END)
        ProgressBar.insert(END, "Must contain a number up to four decimal places")
        return False
    else:
        if not ((float(MassEntry.get()) > 0) and (float(MassEntry.get()) < 100) and (float(LumEntry.get()) < 100000) and
                (float(LumEntry.get()) > 0) and (float(TempEntry.get()) > 3000) and (float(TempEntry.get()) < 10000)):
            ProgressBar.delete(1.0, END)
            ProgressBar.insert(END, "Mass, Temperature, and/or Luminosity are invalid")
            return False
        else:
            if (float(XEntry.get()) >= 0) and (float(ZEntry.get()) >= 0) and (float(MaxPeriodEntry.get()) >= 0) and \
                    (float(MaxAmpEntry.get()) >= 0):
                return True


def override():
    fileIo.set("F")
	
def graphing():
	h = mr.MesaData('LOGS/history.data')
	r1 = h.data(comboBox1.get())
	r2 = h.data(comboBox2.get())
	pl.plot(r1, r2)
	pl.xlabel(comboBox1.get())
	pl.ylabel(comboBox2.get())
	pl.gca().invert_xaxis()
	pl.show()


def linking():
    fff = fileIo.get()
    if fff == "InputFile":
        daf = field.get()
        try:
            file = open(daf, "r")
            corrr = file.readline().strip("\n")

            if corrr != "RR" and corrr != "C":
                ProgressBar.delete(1.0, END)
                ProgressBar.insert(END, "Invalid value for pulsar type. Must be 'C' or 'RR'")
                return

            mass = float(file.readline())
            if mass < 0 or mass > 100:
                ProgressBar.delete(1.0, END)
                ProgressBar.insert(END, "Mass must be between 0 and 100")
                return

            temperature = float(file.readline())
            if temperature < 3000 or temperature > 10000:
                ProgressBar.delete(1.0, END)
                ProgressBar.insert(END, "Temperature must be between 3000 and 10000")
                return

            luminosity = float(file.readline())
            if luminosity < 0 or luminosity > 100000:
                ProgressBar.delete(1.0, END)
                ProgressBar.insert(END, "Luminosity must be between 0 and 100000")
            x = float(file.readline())
            y = float(file.readline())
            period = float(file.readline())
            amp = float(file.readline())

            py = Pulsar(mass, luminosity, x, y, corrr, amp, period, temperature)
            ProgressBar.delete(1.0, END)
            ProgressBar.insert(END, "Pulsar created successfully")

        except FileNotFoundError:
            ProgressBar.delete(1.0, END)
            ProgressBar.insert(END, "File not found.")

        except ValueError:
            ProgressBar.delete(1.0, END)
            ProgressBar.insert(END, "All values in file must be numbers except pulsar type")
    else:
        if name == "L":
            ProgressBar.delete(1.0, END)
            ProgressBar.insert(END, "A pulsar must be selected")
            return None
        if helper():
            pulsar = Pulsar(float(MassEntry.get()), float(LumEntry.get()), float(XEntry.get()), float(ZEntry.get()), name,
                            float(MaxAmpEntry.get()), float(MaxPeriodEntry.get()), float(TempEntry.get()))
            notification_message = "Successfully created a Cepheid" if name == "C" else "Successfully created an RR-Lyrae"
            ProgressBar.delete(1.0, END)
            ProgressBar.insert(END, notification_message)
            Pulsar.editFiles(pulsar)
            return pulsar
        else:
            return None


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
    canvas.create_image(loc[0] + figure_w / 2, loc[1] + figure_h / 2, image=photo)

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
f1 = ttk.Frame(n)
f2 = ttk.Frame(n)
n.add(f1, text='Input Tab')
n.add(f2, text='Output Tab')
n.select(f1)
n.enable_traversal()

fileIo = StringVar()
fileIo.set("F")

var = StringVar()
var.set("L")

R1 = Radiobutton(f1, text="Cepheid", variable=var, value="C", command=override)
R1.pack(anchor=W)
R2 = Radiobutton(f1, text="RR-Lyrae", variable=var, value="RR", command=override)
R2.pack(anchor=W)

fr = Frame(f1, width=200, height=200, borderwidth=2, relief="ridge")
fr.place(x=250, y=67)
R3 = Radiobutton(fr, text ="Input File", variable=fileIo, value="InputFile", command=None)
R3.pack( anchor = W, padx=0, pady=5 )
fileLabel = Label(fr, text="File Address")
fileLabel.pack( anchor = W )
field = Entry(fr, bd=2)
field.pack( anchor = W )

MassLabel = Label(f1, text="Mass")
MassLabel.pack(anchor=W)
MassEntry = Entry(f1, bd=2)
MassEntry.pack(anchor=W)

TempLabel = Label(f1, text="Temperature")
TempLabel.pack(anchor=W)
TempEntry = Entry(f1, bd=2)
TempEntry.pack(anchor=W)

LumLabel = Label(f1, text="Luminosity")
LumLabel.pack(anchor=W)
LumEntry = Entry(f1, bd=2)
LumEntry.pack(anchor=W)

XLabel = Label(f1, text="Hydrogen Composition")
XLabel.pack(anchor=W)
XEntry = Entry(f1, bd=2)
XEntry.pack(anchor=W)

ZLabel = Label(f1, text="Metal Composition")
ZLabel.pack(anchor=W)
ZEntry = Entry(f1, bd=2)
ZEntry.pack(anchor=W)

MaxPeriodLabel = Label(f1, text="Max Period")
MaxPeriodLabel.pack(anchor=W)
MaxPeriodEntry = Entry(f1, bd=2)
MaxPeriodEntry.pack(anchor=W)

ProgressBar = Text(f1, height=1, width=50)
ProgressBar.pack(side=LEFT)
quote = "Something is happening"
ProgressBar.insert(END, quote)

# Creates a pulsar object
submit = Button(f1, text="Submit", command=linking)
submit.pack(side=BOTTOM)

values_list=["model_number","star_age","star_age_day",
                "rsp_phase","rsp_GREKM","rsp_GREKM_avg_abs","rsp_DeltaR",
                "rsp_DeltaMag","rsp_period_in_days","rsp_num_periods",
                "log_dt_sec","radius","log_R","v_surf_km_s",
                "v_surf_div_escape_v","v_div_csound_surf","v_div_csound_max",
                "max_abs_v_div_cs","dt_div_min_dr_div_cs","luminosity",
                "gravity","log_L","effective_T","log_g","log_Teff",
                "photosphere_L","photosphere_r","photosphere_T",
                "photosphere_v_km_s","photosphere_v_div_cs",
                "log_lum_band V","log_lum_band I","log_lum_band bb_V",
                "log_lum_band bb_I","num_retries"]

comboBox1 = ttk.Combobox(f2, values = sorted(values_list))
comboBox2 = ttk.Combobox(f2, values = sorted(values_list))

xLabel = Label(f2, text = "X Value")
xLabel.pack(anchor=W)
comboBox1.pack(anchor=W, padx=5, pady=10)
comboBox1.current(0)
        
yLabel = Label(f2, text = "Y Value")
yLabel.pack(anchor=W)
comboBox2.pack(anchor=W, padx=5, pady=10)
comboBox2.current(0) 

submit2 = Button(f2, text="Make Graph", command=graphing)
submit2.pack(side=BOTTOM)

root.mainloop()