###Thinking & Testing: True or False
###https://www.codewars.com/kata/56d931ecc443d475d5000003

def testit(n):
    '''Returns the number of 0's in the binary form of n'''
    return bin(n)[1:].count('1')