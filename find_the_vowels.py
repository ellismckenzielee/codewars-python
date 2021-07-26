#Find the vowels kata
#https://www.codewars.com/kata/5680781b6b7c2be860000036

def vowel_indices(word):
    return [i + 1 for i, letter in enumerate(word) if letter.lower() in 'aeiouy']