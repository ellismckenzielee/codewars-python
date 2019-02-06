def count_sheep(n):
    '''Return a sheep string depending on integer given '''
    return  ''.join([(str(c) + ' sheep...') for c in list(range(1,n+1))])