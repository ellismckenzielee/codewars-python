#crypanalysis word patterns kata
#https://www.codewars.com/kata/5f3142b3a28d9b002ef58f5e

def word_pattern(word):
    output = ''
    conversion = []
    word = word.lower()
    for letter in word:
        if letter not in conversion:
            conversion.append(letter)       
        output += str(conversion.index(letter)) +'.'
    return output[:-1]