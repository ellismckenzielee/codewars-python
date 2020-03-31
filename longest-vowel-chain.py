###Longest Vowel Chain - codewars kata
###https://www.codewars.com/kata/59c5f4e9d751df43cf000035

import re
def solve(s):
    '''Find and returns the length of the longest chain of vowels within s'''
    matches = re.findall('[aeiou]+', s)
    return max(list(map(len, matches)))