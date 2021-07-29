#filling an array (part 2) kata
#https://www.codewars.com/kata/571e9af407363dbf5700067c

import random 
def squares(n):
    '''Returns the first n numbers squared.'''
    return [x**2 for x in range(1, n+1)]

def num_range(n, start, step):
    '''Returns n numbers based on start and step size.'''
    return list(range(start, start+(step*(n-1))+1, step))

def rand_range(n, mn, mx):
    '''Returns n random numbers between mn and mx (inclusive).'''
    return [random.randrange(mn, mx+1) for x in range(n)]

def primes(n):
    '''Returns the first n prime numbers.'''
    output = []
    counter = 2
    while len(output) < n:
        for num in range(1, counter+1):
            if ((counter % num) == 0) and (num != 1) and (num != counter):
                print(True)
                break
            elif num == counter:
                output.append(counter)
        counter += 1
    return output
            