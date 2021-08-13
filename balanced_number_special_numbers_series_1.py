#balanced number (special numbers series #1) kata
#https://www.codewars.com/kata/5a4e3782880385ba68000018

def balanced_num(number):
    number = list(str(number))
    if len(number) in [1,2]:
        return 'Balanced'
    elif len(number) % 2 == 0:
        midpoint = int(len(number)/2)
        LHS = number[0:midpoint-1]
        RHS = number[midpoint+1:]
    else:
        midpoint = int(len(number)/2)
        LHS = number[0:midpoint]
        RHS = number[midpoint+1:]
    LHS = sum(list(map(int, LHS)))   
    RHS = sum(list(map(int, RHS)))
    if RHS == LHS:
        return 'Balanced'
    else:
        return 'Not Balanced'
    