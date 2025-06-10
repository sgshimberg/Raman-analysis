import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

# Example data (replace this with file reading output)
value_x = []
value_y = []
db=r"D:\NQERG\Raman\BZT080-BCT020-laser-45_RamanShift__0__21-37-25-366.txt"
data_start = False
with open(db , "r") as file:
    for line in file:
        if line.strip() == ">>>>>Begin Spectral Data<<<<<":
            data_start=True
            continue
        if data_start:
            value=[]
            value= (line.strip().split())
            value_x.append(float(value[0]))
            value_y.append(float(value[1]))


peaks, _ = find_peaks(value_y, height=10000, prominence=500)


plt.plot(value_x, value_y)
plt.title("Raman Spectrum")
plt.xlabel("Raman Shift (cm⁻¹)")
plt.ylabel("Intensity (a.u.)")
plt.plot([value_x[i] for i in peaks], [value_y[i] for i in peaks], "ro")
plt.title("Peak Detection")
plt.show()
