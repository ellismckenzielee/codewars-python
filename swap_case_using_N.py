#swap case using N kata
#https://www.codewars.com/kata/5f3afc40b24f090028233490

def swap(s,n):
    s = list(s)
    n = list(bin(n).split('b')[1])
    count = 0
    output = []
    for letter in s:
        if n[count%len(n)] == '1':
            output.append(letter.swapcase())
        else:
            output.append(letter)
        if letter.isalnum():
            count += 1
    return ''.join(output)