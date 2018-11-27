# -*- coding: utf-8 -*-
##
##  Author:     Emil Svendsen
##  Date:       20/11-2018
##  Last edit:  20/11-2018

import scipy.signal as signal
import scipy.fftpack as fft
 
import numpy as np
import matplotlib.pyplot as plt

Ts = 1e-4

fpass = 100
## fstop < 2*fc
fstop = 3000

fcutoff = 100
deltaf = 3

N = np.ceil(3.3/deltaf) + np.mod(np.ceil(3.3/deltaf)+1, 2)
M = int((N - 1)/2)
n = np.matrix.flatten(np.arange(-M, M+1), order='F')

omegaCutOff = 2 * np.pi * fcutoff * Ts
h = np.divide(np.sin(np.multiply(omegaCutOff, n)), np.multiply(np.pi, n))
h[M] = omegaCutOff / np.pi ## When n is zero 

hamWin = signal.windows.hamming(int(N))
hWin = np.multiply(h, hamWin)

print(hWin)


w, h2 = signal.freqz(h)


fig = plt.figure()
plt.title('Digital filter frequency response')
ax1 = fig.add_subplot(111)

plt.plot(w, 20 * np.log10(abs(h2)), 'b')
plt.ylabel('Amplitude [dB]', color='b')
plt.xlabel('Frequency [rad/sample]')

ax2 = ax1.twinx()
angles = np.unwrap(np.angle(h2, deg=True))
plt.plot(w, angles, 'g')
plt.ylabel('Angle (Degrees)', color='g')
plt.grid()
plt.axis('tight')
plt.show()