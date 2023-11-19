# highest Rank Number in an Array kata
# https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004/train/python

from functools import cmp_to_key

def sorter(a, b):
    if a[1] != b[1]:
        return b[1] - a[1]
    return b[0] - a[0]

def highest_rank(arr):
    num_frequency = {}
    for num in arr:
        if num in num_frequency:
            num_frequency[num] += 1
        else:
            num_frequency[num] = 0
    return sorted([(key, value) for key, value in num_frequency.items()], key=cmp_to_key(sorter))[0][0]
