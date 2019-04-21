def mxdiflg(a1, a2):
    '''Find the largest difference between the length of two strings from a1 and a2'''
    if a1 == [] or a2 == []:
        return -1
    x = len(min(a1, key=len))
    y = len(max(a2, key=len))
    result1 = abs(x-y)
    x = len(max(a1, key=len))
    y = len(min(a2, key=len))
    result2 = abs(y-x)
    return result1 if result1 >= result2 else result2