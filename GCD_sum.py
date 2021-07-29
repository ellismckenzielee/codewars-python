#GCD sum kata
#https://www.codewars.com/kata/5dd259444228280032b1ed2a

def solve(s,g):
    for i in range(g, s+1, g):
        remainder = s - i
        if remainder % g == 0:
            return (i, remainder)
    return -1