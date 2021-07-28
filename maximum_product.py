#maximum product kata
#https://www.codewars.com/kata/5a4138acf28b82aa43000117

def adjacent_element_product(array):
    return max(map(lambda x: x[0]*x[1], zip(array[0:-1], array[1:])))