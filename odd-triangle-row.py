###Row of the odd triangle kata
###https://www.codewars.com/kata/5d5a7525207a674b71aa25b5

def odd_row(n):
    '''Returns the row (n) of an odd triangle'''
    multipliers = list(map(lambda x: x*2, list(range(n))))
    start = sum(multipliers) + 1
    return list(range(start, start + (2*n), 2))