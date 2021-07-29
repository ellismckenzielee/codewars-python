#simple equation reversal kata
#https://www.codewars.com/kata/5aa3af22ba1bb5209f000037

def solve(eq):
    output = ""
    numbers = ""
    for char in list(eq[::-1]):
        if char not in ['0','1','2','3','4','5','6','7','8','9']:
            output += ''.join(list(numbers)[::-1])
            output += (char)
            numbers = ""
        else:
            numbers += char
    output += numbers[::-1]
    return output
    