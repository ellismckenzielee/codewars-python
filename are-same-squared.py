
#ARE THEY THE "SAME" KATA
##Checks whether the elements in b are the elements in a squared, 
##regardless of the order

def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    square_values = [x**2 for x in array1]
    for num in array2:
        if num not in square_values:
            return False
        else:
            square_values.remove(num)
    return True