###Largest Product in a Series - codewars kata
###https://www.codewars.com/kata/529872bdd0f550a06b00026e/solutions/python

import numpy as np
def greatest_product(n):
    '''Returns the greatest product of five consecutive numbers in
    n'''
    n = np.array(list(map(int, n)))
    roll_array = np.copy(n)
    for num in range(4):
        roll_array = np.roll(roll_array, -1)
        n = n*roll_array
    return np.max(n[0:-4])