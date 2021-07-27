#sum two arrays kata
#https://www.codewars.com/kata/59c3e8c9f5d5e40cab000ca6

def sum_arrays(array1,array2):
    total = 0
    if array1 != []:
        array1 = ''.join(map(str,array1))
        total += int(array1)
        
    if array2 != []:
        array2 = ''.join(map(str,array2))
        total += int(array2)
        
    if array1 == [] and array2 == []:
        return []
    negative = total < 0
    total = list(map(int, list(str(abs(total)))))
    if negative:
        total[0] = total[0]*-1
    return total
