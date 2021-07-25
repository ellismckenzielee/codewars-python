#Search for letters kata
#https://www.codewars.com/kata/52dbae61ca039685460001ae

def change(st):
    output = [0 for i in range(0, 26)]
    for letter in st:
        condition1, condition2 = [(65 <= ord(letter)), (ord(letter) <= 90)], [(97 <= ord(letter)), (ord(letter) <= 122)]
        if all(condition1) or all(condition2):
            letter = ord(letter.lower())
            output[letter-97] = 1
    return ''.join(list(map(str, output)))