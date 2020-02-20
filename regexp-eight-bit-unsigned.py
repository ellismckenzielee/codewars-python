###Regexp Basics - Codewars kata
###https://www.codewars.com/users/ellismckenzielee/completed_solutions

def eight_bit_number(n):
    '''Returns True if n is an 8-bit unsigned number, else False'''
    if not n.isalnum():
        return False
    n_int = int(n)
    return True if (len(str(n_int)) == len(n) and n_int > -1 and n_int < 256) else False
   
        