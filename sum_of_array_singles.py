#sum of array singles kata
#https://www.codewars.com/kata/59f11118a5e129e591000134

from collections import Counter
def repeats(arr):
    counts = Counter(arr)
    print(counts)
    total = 0
    for key, count in counts.items():
        if count == 1:
            total += key
    return total