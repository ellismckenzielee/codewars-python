def add(n):
    '''Function that returns a function that adds n to any number'''
    def add2(k):
        return n + k
    return add2