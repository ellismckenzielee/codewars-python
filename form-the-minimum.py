###Form the Minimum - codewars kata
###https://www.codewars.com/kata/5ac6932b2f317b96980000ca

def min_value(digits):
    '''Returns the smallest number that could be formed using unique values in digits'''
    digits = sorted(list(set(digits)))
    return int(''.join(list(map(str,digits))))