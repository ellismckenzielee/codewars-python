# Simple Fun #110: Array Operations
# https://www.codewars.com/kata/589aca25fef1a81a10000057/train/python/652d7e547e92f3209537cb05

def array_operations(a, k): 
    k = 1 if k % 2 else 2
    while k > 0:
        maximum = max(a)
        a = list(map(lambda elem: maximum - elem, a))
        k -=1
    return a
