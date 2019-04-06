def solution(string, ending):
    '''Checks to see if the string ends in ending, and returns
    True or False'''
    return True if string[-len(ending):] == ending else False