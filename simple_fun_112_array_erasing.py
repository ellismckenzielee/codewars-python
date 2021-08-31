#simple fun #112: array erasing kata
#https://www.codewars.com/kata/589d1c08cc2e997caf0000e5

from itertools import groupby, chain
def array_erasing(lst):
    runs = 0
    while lst:
        groups = [list(g) for _, g in groupby(lst)]
        candidates = [i for i, g in enumerate(groups) if len(g) > 1]
        i = min(candidates, key=lambda k:abs(len(groups)/2-k)) if candidates else len(groups)//2
        lst = list(chain.from_iterable(groups[:i] + groups[i+1:]))
        runs += 1
    return runs
