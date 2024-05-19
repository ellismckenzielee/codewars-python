# Hofstadter Q
# https://www.codewars.com/kata/5897cdc26551af891c000124/train/python

from functools import cache
import sys 

sys.setrecursionlimit(10000)

@cache
def hofstadter_Q(n):
    if n in [1,2]:
        return 1 
    else:
        return hofstadter_Q(n - hofstadter_Q(n-1)) + hofstadter_Q(n - hofstadter_Q(n-2))
