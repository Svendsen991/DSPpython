# -*- coding: utf-8 -*-
##
##  Author:     Emil Svendsen
##  Date:       20/11-2018
##  Last edit:  20/11-2018

import scipy as sci 
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
g = np.ones(int(T / Ts), order = 1)

## Makes one big matrix size (g x a)
x = np.outer(g, a)
## Make it into one big 1D array
x = np.matrix.flatten(x)
## Makes one big matrix size (g x b)
y = np.outer(g, b)
## Make it into one big 1D array
y = np.matrix.flatten(y)

## Number of samples
Nsamples = (T / Ts) * Nbits

## Time vector
t = np.arange(0, (Nsamples - 1) * Ts, Ts)

## Carrier frequency
fc = 2000




