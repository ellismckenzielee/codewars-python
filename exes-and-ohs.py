def xo(s):
    '''Checks if a string has the same amount of x and o's'''
    x_count = 0
    o_count = 0
    for i in s:
        if (i == 'x' or i == 'X'):
            x_count+=1
        elif (i == 'o' or i == 'O'):
            o_count+=1
            
    if ((x_count == o_count) or ((x_count and o_count) == 0)): 
        return True
    else:
        return False