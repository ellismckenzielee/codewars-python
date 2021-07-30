#evenly distribute values in array kata
#https://www.codewars.com/kata/5bb50eb68f8bbdb4b300021d

def distribute_evenly(lst):
    itms = []
    output = []
    for itm in lst:
        if itm not in itms:
            itms.append(itm)
            
    while len(lst) > 0:
        for itm in itms:
            if itm in lst:
                del lst[lst.index(itm)]
                output.append(itm)
    return output