##SIMPSONS RULS - APPROXIMATE INTEGRATION KATA
##Given n, use simpsons rule to integrate between 0 and pi
##The function is 3/2 * sin^3x

import numpy as np
import math
def simpson(n):
    fa = function(0)
    fb = function(math.pi)
    h = math.pi/n
    first_term_i = ((2*np.arange(1,(n/2)+1))-1)*h
    second_term_i = (2*np.arange(1, n/2)*h)
    return (fa + fb + (4*np.sum(function(first_term_i))) + 2*np.sum(function(second_term_i)))*(math.pi/(3*n))
    
def function(arr):
    return (3/2)*(np.sin(arr))**3