import numpy as np
from numpy import inf 
def doubles(maxk, maxn):
    '''Calculates the force of a box of magnets. See Magnet particules in boxes
    for more details'''
    total_force = 0
    for k in range(1, maxk+1):
        total = (1/(k*np.arange(2, maxn+2)**(2*k)))
        total[total == inf] = 0
        total_force += np.sum(total)
    return total_force