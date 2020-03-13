###Alternate capitalisation - codewars kata
###https://www.codewars.com/kata/59cfc000aeb2844d16000075

def capitalize(s):
    '''Returns two strings based on s. In one case, numbers at an 
    even index are capitalised, and in the second case, the opposite is true'''
    even = ''.join([letter.capitalize()  if i % 2 == 0 else letter for i, letter in enumerate(s)])
    odd = ''.join([letter.capitalize()  if i % 2 == 1 else letter for i, letter in enumerate(s)])
    return [even, odd]