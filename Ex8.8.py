# -*- coding: utf-8 -*-

#   High pass chebyshev
#   Cutoff: 3kHz
#   Passband ripple: 1dB
#   Sampling freq: 8000 Hz


from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

fs = 8000
N = 512
df = (fs/2) / N
f = np.arange(0, fs / 2, df)

B, A = signal.lp2hp([1.9652],[1, 1.9652], wo = 38627)
b, a = signal.bilinear(B, A, fs)

print(b,a)

w, h = signal.freqz(b, a, N)


fig = plt.figure()
plt.title('Digital filter frequency response')
ax1 = fig.add_subplot(111)

plt.plot(f, 20 * np.log10(abs(h)), 'b')
plt.ylabel('Amplitude [dB]', color='b')
plt.xlabel('Frequency [Hz]')

ax2 = ax1.twinx()
angles = np.unwrap(np.angle(h, deg=True))
plt.plot(f, angles, 'g')
plt.ylabel('Angle (Degrees)', color='g')
plt.grid()
plt.axis('tight')
plt.show()