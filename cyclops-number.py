###Cyclops Numbers - codewars kata
###https://www.codewars.com/kata/56b0bc0826814364a800005a


def cyclops (n):
    '''Returns True or False depending on whether a number 
    is a cyclops number. See link'''
    bin_n = bin(n).split('b')[1]
    cond_1 = (len(bin_n) % 2 == 1)
    if '0' in bin_n:
        cond_2 = (bin_n.index('0') + 1 == 1 + len(bin_n) // 2)
    else:
        cond_2 = False
    return True if cond_1 and cond_2 else False