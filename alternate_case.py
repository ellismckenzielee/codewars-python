#alternate case kata
#https://www.codewars.com/kata/57a62154cf1fa5b25200031e

def alternateCase(s):
    return s.swapcase()

def alternateCase(s):
    return ''.join([char.lower() if char.isupper()  else char.upper() for char in s ])