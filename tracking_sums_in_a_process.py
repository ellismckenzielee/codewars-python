#Tracking Sumns in a Process kata
#https://www.codewars.com/kata/56dbb6603e5dd6543c00098d

def unique_filter(arr):
    seen = set()
    return [x for x in arr if not (x in seen or seen.add(x))]

def track_sum(arr):
    sums = []
    unique = unique_filter(arr)
    srted = sorted(unique,reverse=True)
    subtracted = list(map(lambda x: x[0] - x[1], zip(srted[:-1], srted[1:])))
    unique2 = unique_filter(subtracted)
    return [[sum(arr), sum(unique), sum(subtracted), sum(unique2)], unique2]
    