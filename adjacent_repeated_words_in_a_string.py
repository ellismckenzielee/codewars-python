#adjacent repeated words in a string kata
#https://www.codewars.com/kata/5245a9138ca049e9a10007b8

from itertools import groupby
def count_adjacent_pairs(st): 
    lst = list(map(lambda x: x.lower(), st.split(" ")))
    total = 0
    for _, g in groupby(lst):
        if len([group for group in g]) > 1:
            total +=1
    return total