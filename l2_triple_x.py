#L2: Triple X kata
#https://www.codewars.com/kata/568dc69683322417eb00002c

def triple_x(s):
    for i, elem in enumerate(s[:-2]):
        if elem == 'x':
            return elem == s[i+1] and elem == s[i+2]
    return False
        