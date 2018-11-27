# -*- coding: utf-8 -*-
##
##  Author:     Emil Svendsen
##  Date:       27/11-2018
##  Last edit:  27/11-2018
##  
##  QPSK


import scipy.signal as signal
import scipy.fftpack as fft
 
import numpy as np
import matplotlib.pyplot as plt

import lowpass

a = np.add(np.multiply(2, [1,1,0,0,1,1,0,0]), -1)
b = np.add(np.multiply(2, [1,0,1,0,1,0,1,0]), -1)

Nbits = len(a)

## Pulse length
T = 0.01
## Sampling periode
Ts = 1e-4
## Sampling frequency
fs = 1 / Ts

## Makes 1D array with length of (T / Ts)
g = np.ones(int(T / Ts))


## Makes one big matrix size (g x a)
x = np.outer(g, a)
## Make it into one big 1D array
x = np.matrix.flatten(x, order='F')
## Makes one big matrix size (g x b)
y = np.outer(g, b)
## Make it into one big 1D array
y = np.matrix.flatten(y, order='F')

## Number of samples
Nsamples = (T / Ts) * Nbits
## Time vector
t = np.arange(0, (Nsamples) * Ts, Ts)

## Carrier frequency
fc = 2000

## Carrier waves
cosfc = np.cos(2 * np.pi * fc * t)
sinfc = np.sin(2 * np.pi * fc * t)

## Element wise multiply and add
v = np.add(np.multiply(x, cosfc), np.multiply(y, sinfc))

## Frequency definition # Sample frequency / Nsamples
df = fs / Nsamples

## Only positive frequencies
f = np.arange(0, (df * Nsamples / 2), df)
## Only negative frequencies
fNeg = np.multiply(np.fliplr([np.arange(0+df, (df * Nsamples / 2) + df, df)]), -1)
## All frequencies
f = np.concatenate((fNeg, f), axis = None)


## Demodulate 
i = np.multiply(v, cosfc)
q = np.multiply(v, sinfc)

## Lowpass
test1 = lowpass.lowpass(i, Ts, fs, 1000)
test2 = lowpass.lowpass(q, Ts, fs, 1000)



plt.subplot(4,2,1)
plt.plot(x)
plt.subplot(4,2,2)
plt.plot(y)
plt.subplot(4,2,3)
plt.plot(t, np.multiply(x, cosfc))
plt.subplot(4,2,4)
plt.plot(t, np.multiply(y, sinfc))
plt.subplot(4,2,5)
plt.plot(t, i)
plt.subplot(4,2,6)
plt.plot(t, q)
plt.subplot(4,2,7)
plt.plot(t, test1[np.arange(0,800)])
plt.subplot(4,2,8)
plt.plot(t, test2[np.arange(0,800)])


plt.show()