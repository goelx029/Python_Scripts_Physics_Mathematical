import matplotlib.pyplot as plt
from math import *
import numpy as np

def DegreeToRad(deg):
    return (deg/180)*pi

longitude = np.array([322, 327, 330, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 340, 345, 350, 355])
newLongitude = longitude + 32
R = 8.5*np.sin(DegreeToRad(newLongitude))
Vs = np.array([-10, 5, 0, 25, 50, 35, 75, 65, 50, 25, 10, 5, 2, 4, -10, 25, 25, 15, 30])
Vr = Vs + 220*np.sin(DegreeToRad(newLongitude))
plt.plot(abs(R), Vr, 'ro')
plt.xlabel("R in kpc")
plt.ylabel("Vcircular in ")
plt.show()
