###Difference of Two - codewars kata
###https://www.codewars.com/kata/5340298112fa30e786000688

def twos_difference(lst): 
    '''Returns pairs of integers in list that have a difference of two'''
    output = []
    for num in sorted(lst):
        if num + 2 in lst:
            output.append((num, num+2))
    return output