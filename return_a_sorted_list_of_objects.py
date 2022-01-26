## return a sorted list of objects kata
## https://www.codewars.com/kata/52705ed65de62b733f000064


def sort_list(sort_by, lst):
    sorted_lst = sorted(lst, key=lambda obj: obj[sort_by], reverse=True) 
    return sorted_lst
