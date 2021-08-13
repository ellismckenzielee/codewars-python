#absent vowel kata
#https://www.codewars.com/kata/56414fdc6488ee99db00002c

def absent_vowel(x): 
    letters = set(x)
    for i, vowel in enumerate(['a','e','i','o','u']):
        if vowel not in letters:
            return i