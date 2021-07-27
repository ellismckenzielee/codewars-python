#simple reversed paranthesis kata
#https://www.codewars.com/kata/5a3f2925b6cfd78fb0000040

def solve(s):
    previous_modified, total = s, 0
    if len(s) % 2 == 1:
        return -1
    else:
        while True:
            modified = previous_modified.replace('()', '')
            if modified == previous_modified:
                break
            else:
                previous_modified = modified
    for i in range(0, len(modified) -1, 2):
        res = modified[i] + modified[i+1]
        if res == ')(':
            total += 2
        elif res != '()':
            total += 1
    return total