#thinking and testing: uniq or not uniq kata
#https://www.codewars.com/kata/56d949281b5fdc7666000004

def testit(a, b):
    a = list(set(a))
    b = list(set(b))
    a.extend(b) 
    return sorted(a)