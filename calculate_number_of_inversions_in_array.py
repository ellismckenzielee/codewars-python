#calculate number of inversions in array kata
#https://www.codewars.com/kata/537529f42993de0e0b00181f

import numpy as np
def count_inversions(array):
    array = np.array(array)
    total = 0
    for i in range(len(array)):
        num = array[i] 
        total += np.sum(array[i+1:] < num)
    return total
    