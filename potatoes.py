def potatoes(p0, w0, p1):
    '''Returns mass of dried potatoes, based on the percentage water before and after'''
    return int(((w0*100)-(p0*w0))/(100-p1))