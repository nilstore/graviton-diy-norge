# Python + PySerial + Arduino Due for 1 MHz sampling
import serial
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

ser = serial.Serial('COM4', 2000000)  # Due native port
data = np.frombuffer(ser.read(1000000), dtype=np.int16)

f, Pxx = welch(data - data.mean(), fs=1e6, nperseg=16384)
plt.loglog(f, np.sqrt(Pxx)*1e-15/1e-3)  # konverter til m/√Hz
plt.axhline(1e-15, color='r', ls='--')
plt.show()