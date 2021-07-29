#simple consecutive pairs kata
#https://www.codewars.com/kata/5a3e1319b6486ac96f000049

def pairs(ar):
    total = 0
    for i in range(0, len(ar)-1,2):
        if abs(ar[i] - ar[i+1]) == 1:
            total += 1
    return total
        