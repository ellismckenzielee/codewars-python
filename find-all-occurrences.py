###Find All Occurrences of an Element in an array - codewars kata
###https://www.codewars.com/kata/59a9919107157a45220000e1

def find_all(array, n):
    '''Returns the number of times that n appears in array'''
    indeces = []
    for i, num in enumerate(array):
        if num == n:
            indeces.append(i)
    return indeces