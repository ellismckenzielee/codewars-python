#find within array kata
#https://www.codewars.com/kata/51f082ba7297b8f07f000001

def find_in_array(seq, predicate): 
    if seq:
        for i, item in enumerate(seq):
            if predicate(item, i) == True:
                return i 
    return -1