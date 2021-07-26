#Simple Fun #136: Missing Values kata
#https://www.codewars.com/kata/58a66c208b88b2de660000c3

from collections import Counter
def missing_values(seq): 
    counts = Counter(seq)
    vals = [item for item, count in sorted(counts.items(), key=lambda x: x[1])]
    return vals[0] * vals[0] * vals[1] 