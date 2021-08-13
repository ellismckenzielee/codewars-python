#primordial of a number kata
#https://www.codewars.com/kata/5a99a03e4a6b34bb3c000124

import numpy as np

def num_primorial(n):
    total = 1
    prime_number_count = 0
    number = 2
    while prime_number_count < n:
        if is_prime(number) == True:
            total *= number
            prime_number_count += 1
        number += 1
      
    return total
    
def is_prime(num):
    remainders =num % np.arange(1, num+1)
    return len(remainders[remainders == 0]) == 2
    