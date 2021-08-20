#simple fun #152: invite more women? kata
#https://www.codewars.com/kata/58acfe4ae0201e1708000075

def invite_more_women(arr):
    return not arr.count(-1) >= arr.count(1)