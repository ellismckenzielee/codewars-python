###Enumerable Magic #5 - True for Just One? - codewars kata
###https://www.codewars.com/kata/54599705cbae2aa60b0011a4

def one(sq, fun): 
    '''Returns True if the function fun, applied to each element of 
    sq, returns True only in one instance'''
    return list(map(fun, sq)).count(True) == 1