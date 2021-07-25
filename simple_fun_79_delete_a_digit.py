#simple Fun #79: Delete a Digit kata
#https://www.codewars.com/kata/5894318275f2c75695000146

def delete_digit(n):
    n = list(str(n))
    max = 0
    for i, num in enumerate(n):
        res = int(''.join(n[0:i] + n[i+1:]))
        if res > max:
            max = res
    return max