###Bit Counting - codewars kata
###https://www.codewars.com/kata/526571aae218b8ee490006f4

def countBits(n):
    '''Returns the number of 1's in binary representation
    of a number'''
    return bin(n).split('b')[1].count('1')