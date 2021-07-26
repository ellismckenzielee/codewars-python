#Find the missing letter kata
#https://www.codewars.com/kata/5839edaa6754d6fec10000a2

def find_missing_letter(chars):
    previous = ord(chars[0])-1
    for char in chars:
        if ord(char) != previous + 1:
            return chr(previous+1)
        previous += 1
