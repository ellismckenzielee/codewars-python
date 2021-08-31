#unique in order kata
#https://www.codewars.com/kata/54e6533c92449cc251001667

from itertools import groupby
def unique_in_order(iterable):
    return [elem for elem, _ in groupby(iterable)]
    