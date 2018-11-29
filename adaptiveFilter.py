# -*- coding: utf-8 -*-
##
##  Author:     Emil Svendsen
##  Date:       27/11-2018
##  Last edit:  27/11-2018
##  
##  Adaptive Filter


import scipy.signal as signal
import scipy.fftpack as fft
 
import numpy as np
import matplotlib.pyplot as plt





fs = 80


num_samples = 1000

df = (fs/2) / num_samples
f = np.arange(0, fs / 2, df)


n = np.arange(0, num_samples)

## Signal
s = np.sin(2* np.pi  * f)

## White noise
mean = 0
std = 1 
noise = np.random.normal(mean, std, size=num_samples)

## Signal plus noise
d = s + noise

## Filter wieghts
w = [0.5]
mu = 0.02
y = np.zeros(num_samples)
e = np.zeros(num_samples)

for i in n:
    y[i] = w[0] * noise[i]
    e[i] = d[i] - y[i]
    w[0] = w[0] + 2* mu * (e[i] * noise[i])
    #print(w[0])

plt.subplot(2,2,1)
plt.plot(s)
plt.subplot(2,2,2)
plt.plot(d)
plt.subplot(2,2,3)
plt.plot(y)
plt.subplot(2,2,4)
plt.plot(e)


plt.show()