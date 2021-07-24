#String letter counting kata
#https://www.codewars.com/kata/59e19a747905df23cb000024

def string_letter_count(s):
    output = ''
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        total = s.count(letter.upper()) + s.count(letter.lower())
        if total > 0:
            output += str(total)+ letter
    return output
        