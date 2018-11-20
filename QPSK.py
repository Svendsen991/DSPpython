# -*- coding: utf-8 -*-
##
##  Author:     Emil Svendsen
##  Date:       20/11-2018
##  Last edit:  20/11-2018

import scipy.signal as signal
import scipy.fftpack as fft
 
import numpy as np
import matplotlib.pyplot as plt

## Random sequence lenght of Nbits
Nbits = 8
a = 2 * np.random.randint(0, 2, Nbits) -1
b = 2 * np.random.randint(0, 2, Nbits) -1

## Pulse length
T = 1
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
cosfc = np.sqrt(2) * np.cos(2 * np.pi * fc * t)
sinfc = np.sqrt(2) * np.sin(2 * np.pi * fc * t)

## Element wise multiply and add
v = np.add(np.multiply(x, cosfc), np.multiply(y, sinfc))

## Frequency definition # Sample rate / Nsamples
df = fs / Nsamples

## Only positive frequencies
f = np.arange(0, (df * Nsamples / 2), df)
## Only negative frequencies
fNeg = np.multiply(np.fliplr([np.arange(0+df, (df * Nsamples / 2) + df, df)]), -1)
## All frequencies
f = np.concatenate((fNeg, f), axis = None)


## Demodulation
i = np.multiply(v, cosfc)
q = np.multiply(v, sinfc)

## Plot
figXY = plt.figure()
plt.title('x and y plot')
## x plot
plt.subplot(4,2,1)
plt.plot(t, x, 'b')
plt.ylabel('x', color='b')
plt.xlabel('Tid [s]')
plt.grid()
plt.axis('tight')
## y plot
plt.subplot(4,2,2)
plt.plot(t, y, 'g')
plt.ylabel('y', color='g')
plt.xlabel('Tid [s]')
plt.grid()
plt.axis('tight')
## x frequency plot
plt.subplot(4,2,3)
plt.plot(f, fft.fftshift(np.abs(fft.fft(x))**2) / Nsamples**2 , 'b')
plt.ylabel('y effekt', color='b')
plt.xlabel('Frekvens [Hz]')
plt.grid()
plt.axis('tight')
#plt.xlim((-5,5))
## y frequency plot
plt.subplot(4,2,4)
plt.plot(f, fft.fftshift(np.abs(fft.fft(y))**2) / Nsamples**2 , 'g')
plt.ylabel('y effekt', color='g')
plt.xlabel('Frekvens [Hz]')
plt.grid()
plt.axis('tight')
#plt.xlim((-5,5))
## v frequency plot
plt.subplot(4,2,5)
plt.plot(f, fft.fftshift(np.abs(fft.fft(v))**2) / Nsamples**2 , 'g')
plt.ylabel('v effekt', color='g')
plt.xlabel('Frekvens [Hz]')
plt.grid()
plt.axis('tight')
## v frequency plot
plt.subplot(4,2,6)
plt.plot(t, v, 'g')
plt.ylabel('v effekt', color='g')
plt.xlabel('Frekvens [Hz]')
plt.grid()
plt.axis('tight')
## i frequency plot
plt.subplot(4,2,7)
plt.plot(f, fft.fftshift(np.abs(fft.fft(i))**2) / Nsamples**2 , 'g')
plt.ylabel('i effekt', color='g')
plt.xlabel('Frekvens [Hz]')
plt.grid()
plt.axis('tight')
#plt.xlim((-5,5))
## q frequency plot
plt.subplot(4,2,8)
plt.plot(f, fft.fftshift(np.abs(fft.fft(q))**2) / Nsamples**2 , 'g')
plt.ylabel('q effekt', color='g')
plt.xlabel('Frekvens [Hz]')
plt.grid()
plt.axis('tight')
#plt.xlim((-5,5))

plt.show()


