# -*- coding: utf-8 -*-
##
##  Author:     Emil Svendsen
##  Date:       20/11-2018
##  Last edit:  20/11-2018

import scipy.signal as signal
import scipy.fftpack as fft
 
import numpy as np
import matplotlib.pyplot as plt



def lowpass(x, Ts, fs, fc):
    ## Sampling periode
    #Ts = 1e-4
    ## Sampling frequency
    #fs = 1 / Ts # Hz
    ## Cutoff frequency
    #fc = 1000 # Hz

    Omega = (fc / fs) * np.pi
    M = 4

    n = np.arange(-M, M + 1)

    ## Prevent error when dividing by zero
    nZeroTable = np.not_equal(n, 0)
    h = np.divide( np.sin(Omega * n), n * np.pi , where = nZeroTable)
    h[M] = Omega / np.pi

    y = np.convolve(h, x)
    return y