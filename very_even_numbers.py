#very even numbers kata
#https://www.codewars.com/kata/58c9322bedb4235468000019

import numpy as np
def is_very_even_number(n):
    n = np.array(list(map(int, list(str(n)))))
    total = np.sum(n)
    if len(n) <2 :
        return total % 2 == 0
    else:
        return is_very_even_number(total)