# -*- coding: utf-8 -*-
##
##  Author:     Emil Svendsen
##  Date:       27/11-2018
##  Last edit:  27/11-2018
##  
##  Noise



import numpy as np

def noise(num_samples):
    ## White noise
    mean = 0
    std = 1 
    noise = np.random.normal(mean, std, size= int(num_samples))
    
    return noise
