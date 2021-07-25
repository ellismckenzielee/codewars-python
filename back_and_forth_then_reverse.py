#Back and forth then reverse! kata
#https://www.codewars.com/kata/60cc93db4ab0ae0026761232

def arrange(s):
    if s == []:
        return []
    t = [s[0]]
    counts = [-1, -2]
    while len(t) < len(s):
        t.append(s[counts[0]])
        t.append(s[counts[1]])
        if counts[0] < 0:
            counts[0] *= -1
            counts[1] *= -1
        else:
            counts[0] = (counts[0] + 2)*-1
            counts[1] = (counts[1] + 2)*-1

    if len(t) > len(s):
        t.pop(-1)

    return t
        
        
    