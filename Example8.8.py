# -*- coding: utf-8 -*-

#   High pass chebyshev
#   Cutoff: 3kHz
#   Passband ripple: 1dB
#   Sampling freq: 8000 Hz

from __future__ import division
import math
from sympy import *

cutoff = 3000
fs = 8000

T = 1/fs
omega_d = 2 * math.pi * cutoff
print("omega d: ", omega_d)
omega_a = (2/T) * math.tan((omega_d * T) / 2)
print("omega a: ",omega_a)

## s = Symbol('s')
s, z = symbols("s, z")## Sub: s = omega_a / s
Hp = 1.9652 / (s + 1.9652), omega_a / s
Hs = Hp.subs(s, omega_a / s)  ## Hp = 1.9652 / (s + 1.9652) from table 8.5
print(Hs)

Hs = 1.9652*s/(1.9652*s + 38627.4169979695)
print(Hs)

Hs = (1.9652*s/1.9652)/((1.9652*s + 38627.4169979695)/1.9652)
print(Hs)


Hz = Hs.subs(s, (2 / T) * ((z)/(z)))
print(Hz)


