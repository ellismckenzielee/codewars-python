#maximum gap (array series #4) kata
#https://www.codewars.com/kata/5a7893ef0025e9eb50000013

import numpy as np
def max_gap(numbers):
    numbers = np.array(sorted(numbers))
    return np.max(numbers[1:]-numbers[:-1])