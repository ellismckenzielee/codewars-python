#even and odd! kata
#https://www.codewars.com/kata/594adadee075005308000122

def even_and_odd(n): 
    evens = list(filter(lambda x: int(x) % 2 ==0, str(n)))
    odds = list(filter(lambda x: int(x) % 2 !=0, str(n)))
    if evens:
        evens = int(''.join(evens))
    else:
        evens = 0
    if odds:
        odds = int(''.join(odds))
    else:
        odds = 0
    return evens,odds