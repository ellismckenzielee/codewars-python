# How many unique consonants kata
# https://www.codewars.com/kata/5a19226646d843de9000007d/solutions/python

def count_consonants(text):
    consonants = []
    for letter in text:
        lowercase_letter = letter.lower()
        if lowercase_letter not in consonants + ['a','e', 'i', 'o', 'u'] and lowercase_letter.isalpha():
            consonants.append(lowercase_letter)
    return len(consonants)
