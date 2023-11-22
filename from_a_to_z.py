# From A to Z kata
# https://www.codewars.com/kata/6512b3775bf8500baea77663/train/python 

def gimme_the_letters(sp):
    first_letter, last_letter = sp.split('-')
    sequence = ''
    for i in range(ord(first_letter), ord(last_letter) + 1):
        sequence += chr(i)
    return sequence
