#the old switcheroo kata
#https://www.codewars.com/kata/55d410c492e6ed767000004f

def vowel_2_index(string):
    output = ''
    for i, char in enumerate(string):
        if char.lower() in 'aeiou':
            char = str(i+1)
        output += char
    return output