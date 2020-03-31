###Array.diff - codewars kata
###https://www.codewars.com/kata/523f5d21c841566fde000009

def array_diff(a, b):
    '''Removes all values from list a, that are present in b'''
    return [x for x in a if x not in b]