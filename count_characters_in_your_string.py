#Count characters in your string kata
#https://www.codewars.com/kata/52efefcbcdf57161d4000091

def count(string):
    chars = set(string)
    diction = {}
    for char in chars:
        diction[char] = string.count(char)
    return diction