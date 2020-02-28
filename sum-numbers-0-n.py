###Sum of numbers from 0 to N - codewars kata
###https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763/python

def show_sequence(n):
    '''Returns a string showing the summation of n to the total'''
    if n < 0:
        strng = '{}<0'.format(n)
    elif n == 0:
        strng = '{}=0'.format(n)
    else:
        total = sum(list(range(n+1)))
        strng = '+'.join(list(map(str, list(range(n+1))))) + ' = {}'.format(str(total))
    return strng