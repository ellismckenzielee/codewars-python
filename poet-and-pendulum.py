###The Poet and The Pendulum - codewars kata 
###https://www.codewars.com/kata/5bd776533a7e2720c40000e5

def pendulum(values):
    '''Returns values sorted, with smallest value at centre of the list and the 
    remaining sorted incrmentally left then right'''
    sorted_values = sorted(values)
    mid = [sorted_values [0]]
    right = sorted_values[1::2]
    left = sorted_values[2::2]
    return left[::-1] + mid + right