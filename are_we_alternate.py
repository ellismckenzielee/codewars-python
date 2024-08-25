# are we alternate? kata
# https://www.codewars.com/kata/59325dc15dbb44b2440000af

def is_alt(s):
    vowels = "aeiou"
    previous_letter_is_vowel = not s[0] in vowels
    for letter in s:
        is_vowel = letter in vowels
        if is_vowel == previous_letter_is_vowel:
            return False
        previous_letter_is_vowel = is_vowel
    return True
        
