def catch_sign_change(lst):
    '''Returns the number of sign changes in a list'''
    if lst == []:
        return 0
        
    previous_greater_than_zero = lst[0] >= 0
    output = 0
    for num in lst:
        print(previous_greater_than_zero)
        if num >= 0:
            current = True
            if current == previous_greater_than_zero:
                continue
            if current != previous_greater_than_zero:
                output +=1
                previous_greater_than_zero = current
        else:
            current = False
            if current == previous_greater_than_zero:
                continue
            if current != previous_greater_than_zero:
                output +=1
                previous_greater_than_zero = current
                
    return output