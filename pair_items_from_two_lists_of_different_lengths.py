#pair items from two lists of different lengths kata
#https://www.codewars.com/kata/61055e2cb02dcb003da50cd5/solutions/python


#REFACTORED VERSION 
from itertools import combinations
def pair_items(list1, list2):
    length = min(len(list1), len(list2))
    comb1 = list(combinations(list1, length))
    comb2 = list(combinations(list2, length))
    output = []
    for com1 in comb1:
        for com2 in comb2:
            output.append(list(zip(com1, com2)))
    return output

from itertools import combinations
def pair_items(list1, list2):
    len_l1 = len(list1)
    len_l2 = len(list2)
    output = []
    if len_l1 == len_l2:
        return [list(zip(list1, list2))]
    elif len_l1 > len_l2:
        l1_combs = list(combinations(list1, len_l2))
        for comb in l1_combs:
            output.append(list(zip(comb, list2)))
    elif len_l2 > len_l1:
        l2_combs = list(combinations(list2, len_l1))
        for comb in l2_combs:
            output.append(list(zip(list1, comb)))
    return output