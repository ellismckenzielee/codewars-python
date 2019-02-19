def contain_all_rots(strng, arr):
    '''Finds if all possible rotations of strng can be found in arr,
       Hope to refactor this soon.'''
    if strng == '':
        return True
    
    str = alphabetic_order(strng)
    
    counter = 0
    
    for string in arr:
        string_sorted = alphabetic_order(string)
        if str in string_sorted:
            counter += 1
    if counter == len((str)):
        return True
    elif counter == len((str))/2:
        return True
    return False
    
def alphabetic_order(str):
    letters = list(str)
    sorted_letters = sorted(letters)
    return ''.join(sorted_letters)