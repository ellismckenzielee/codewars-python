###Maximum Triplet Sum - codewars kata
###https://www.codewars.com/users/ellismckenzielee/completed_solutions

def max_tri_sum(numbers):
    '''Returns the maximum value that can be produced from the summation 
    of unique values in numbers'''
    
    return sum(sorted(set(numbers),reverse = True)[0:3])