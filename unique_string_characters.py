#unique string characters kata
#https://www.codewars.com/kata/5a262cfb8f27f217f700000b

def solve(a,b):
    output = ''
    for letter in a:
        if letter not in b:
            output += letter
    for letter in b:
        if letter not in a:
            output += letter
            
    return output