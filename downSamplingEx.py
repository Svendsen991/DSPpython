# -*- coding: utf-8 -*-

## Downsampling filter

from scipy import signal, fftpack
import numpy as np
import matplotlib.pyplot as plt

## Sampling rate
fs = 8000
## Number of samples
N = 2048
## Downsampling factor
M = 2

n = np.arange(0, N-1, 1)
f = (np.arange(0, (N/2) - 1, 1) * fs / N)

## Input
x = 5 * np.sin((np.pi / 4) * n ) + np.cos((5*np.pi*n) / 8)

## Single sided amplitude spectrum
X = 2*np.abs(fftpack.fft(x, N)) / N
X[0] = X[0] / 2


## Output with sampling rate fs / M
y = x[np.arange(0, N, M)]
NM = len(y)
fsM = np.arange(0, (NM/2)-1, 1) * (fs/M)/NM

## Single sided amplitude spectrum
Y = 2*np.abs(fftpack.fft(y, NM)) / NM
Y[0] = Y[0] / 2


## Plot both spectrums
fig = plt.figure()
plt.title('Digital filter frequency response')
ax1 = fig.add_subplot(111)

plt.plot(f, X[np.arange(0, (N/2) - 1, dtype=int)], 'b')
plt.ylabel('Amplitude X', color='b')
plt.xlabel('Frequency [Hz]')

ax2 = ax1.twinx()
plt.plot(fsM, Y[np.arange(0, (NM/2) - 1, dtype=int)], 'g')
plt.ylabel('Amplitude X / 2', color='g')

plt.grid()
plt.axis('tight')
plt.show()
