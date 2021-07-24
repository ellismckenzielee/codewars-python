#Count letters in string kata
#https://www.codewars.com/kata/5808ff71c7cfa1c6aa00006d

def letter_count(s):
    letters = set(s)
    output = {}
    for letter in letters:
        output[letter] = s.count(letter)
    return output
        