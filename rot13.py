#ROT13 Kata
#https://www.codewars.com/kata/530e15517bc88ac656000716

def rot13(message):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    output = ''
    for letter in message:
        if letter.lower() in alphabet:
            uppercase = letter.isupper()
            index = alphabet.index(letter.lower())
            new_letter = alphabet[(index+13)%len(alphabet)]
            if uppercase:         
                new_letter = new_letter.upper()
            output += (new_letter)
        else:
            output += letter
    return output