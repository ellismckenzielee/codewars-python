#permutations kata
#https://www.codewars.com/kata/5254ca2719453dcc0b00027d

import itertools
def permutations(string):
    perms = itertools.permutations(string, len(string))
    perms = set(list(map(lambda x: ''.join(x), perms)))
    return perms