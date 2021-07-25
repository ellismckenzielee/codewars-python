#Find the unique string kata
#https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3

from collections import Counter
def find_uniq(arr):
    new_arr = []
    for elem in arr:
        new_arr.append(''.join(sorted(list(set(elem.lower())))))
    unique = Counter(new_arr).most_common()
    for i, elem in enumerate(new_arr):
        if unique[1][0] in elem:
            return arr[i]
    