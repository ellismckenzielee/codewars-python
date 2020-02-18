###Solution codewars kata
###Takes a string as input and replaces any camelcase letters with a space and lowercase letter

def solution(s):
    '''Solution returns the formatted string'''
    return  ''.join(list(map(upper, list(s))))
    
def upper(letter):
    '''Converts capital letters to a space and the lower case letter'''
    return ' ' + letter if letter.isupper() else letter