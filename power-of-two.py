def power_of_two(x):
    '''Find if a number can be obtained via 2^n'''
    current_number = 0
    counter = 0
    while current_number <= x:
        current_number = 2**counter
        counter+=1
        if current_number == x:
            return True
    return False   