#Equal sides of an array kata
#https://www.codewars.com/kata/5679aa472b8f57fb8c000047

def find_even_index(arr):
    for i in range(0,len(arr)):
        LHS = sum(arr[:i])
        RHS = sum(arr[i+1:])
        if LHS == RHS:
            return i
    return -1