#number of measurements to spot the counterfeit coin kata
#https://www.codewars.com/kata/59530d2401d6039f8600001f

import numpy as np
def how_many_measurements(n):
    if n <= 3:
        if n == 1:
            return 0
        return 1
    
    num = (np.log((n*3))/np.log(3))
    return int(num)