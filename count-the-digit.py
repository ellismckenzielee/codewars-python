def nb_dig(n, d):
    '''Takes an integer n, calculates the square of each number from one to n, and returns
    how many times d appears'''
    
    values_list = list(range(0, n+1))
    list_squared = list(map(lambda x: str(x**2), values_list))
    str_list_squared = ''.join(list_squared)
    print(str(d))
    return str_list_squared.count(str(d))