#array exchange kata
#https://www.codewars.com/kata/5353212e5ee40d4694001114

def exchange_with(a, b):
    a_len = len(a)
    b_len = len(b)
    a_plc = a.copy()
    b_plc = b.copy()
    
    a.extend(b_plc[::-1])
    del a[0:a_len]
    b.extend(a_plc[::-1])
    del b[0:b_len]
    