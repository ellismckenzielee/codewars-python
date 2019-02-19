def fit_in(a,b,m,n):
    '''See if two squares fit in a suitcase based on dimensions'''
    print(a,b,m,n)
    check_1 = (a + b) <= m
    check_2 = (a+b) <=n
    check_3 = (a <= m) and (a <= n) and  (b <= m) and (b <= n)
    
    if (check_1 == True or check_2 == True) and (check_3 == True):
        return True
        
    return False