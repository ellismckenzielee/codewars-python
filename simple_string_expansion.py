#simple string expansion kata
#https://www.codewars.com/kata/5a793fdbfd8c06d07f0000d5

def solve(st):
    i, st = 0, st[::-1]
    while i < len(st):
        if st[i] == ')':
            output = ''
        elif st[i] == '(':
            if st[i+1] in '0123456789':
                output *= int(st[i+1])
            else:
                output += st[i+1]
            i += 1
        else:
            output += st[i]
        i += 1
    return output[::-1]   