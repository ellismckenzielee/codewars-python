def is_triangle(a, b, c):
    '''Accepts 3 integer values and returns True/False depending on whether a triangle'''
    x = a + b
    y = a + c
    z = b + c
    if (x <= c) or (y <= b) or (z <= a):
        return False
    else:
        return True