#keystroking kata
#https://www.codewars.com/kata/5be085e418bcfd260b000028

def num_key_strokes(text):
    total = 0
    singles = "1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./ `"
    for letter in text:
        total += 1 
        if letter not in singles:
            total += 1
    return total