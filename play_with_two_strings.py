#play with two strings kata
#https://www.codewars.com/kata/56c30ad8585d9ab99b000c54/solutions/python

def work_on_strings(a,b):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    switch_a = []
    switch_b = []
    for letter in alphabet:
        switch_a.append(b.lower().count(letter)%2)
        switch_b.append(a.lower().count(letter)%2)
    concat = a + b
    output = ''
    for i, letter in enumerate(concat):
        if i < len(a):
            if switch_a[alphabet.index(letter.lower())] == 1:
                letter =  letter.swapcase()
        else:
            if switch_b[alphabet.index(letter.lower())] == 1:
                letter =  letter.swapcase()
        output += letter
    return output
    
 