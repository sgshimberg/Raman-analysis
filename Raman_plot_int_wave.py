from seaprease import plot_correction
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

#Create plot window
root = tk.Tk()
root.title("Raman spectra")

data = plot_correction()
spectra = data.plot_array()

print("Data shape: ", spectra.shape)

# Axis data from array
x_axis = spectra[0]
y_axis = spectra[1]

#Create graph 
fig, ax = plt.subplots()
ax.plot(x_axis,y_axis)
ax.set_xlabel("shift cm^-1")
ax.set_ylabel("Intensity")
ax.set_title("Raman Shift Vs Intensity")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

root.mainloop()

plt.close()