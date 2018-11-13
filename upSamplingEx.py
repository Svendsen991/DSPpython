# -*- coding: utf-8 -*-

## Upsampling filter

from scipy import signal, fftpack
import numpy as np
import matplotlib.pyplot as plt

## Sampling rate
fs = 8000
## Number of samples
N = 2048
## Upsampling factor
L = 3

n = np.arange(0, N-1)

## Input

x = 5 * np.sin((np.pi / 4) * n ) + np.cos((5*np.pi*n) / 8)

w = np.zeros(L * N)

for i in n:
    w[L * i] = x[i]

## Length of upsampled data
NL = len(w)

## Single sided amplitude spectrum
W = 2 * np.abs(fftpack.fft(w, NL)) / NL
W[0] = W[0] / 2

## Frequency index
f = np.arange(0, NL / 2 - 1) * fs * L / NL


