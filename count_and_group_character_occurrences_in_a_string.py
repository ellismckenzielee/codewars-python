#count and group character occurrences in a string kata
#https://www.codewars.com/kata/543e8390386034b63b001f31

def get_char_count(s):
    letter_dict = {}
    count_dict = {}
    for letter in s:
        if letter.isalnum():
            letter = letter.lower()
            if letter in letter_dict.keys():
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    
    for letter, counts in letter_dict.items():
        if counts not in count_dict.keys():
            count_dict[counts] = [letter]
        else:
            count_dict[counts].append(letter)
            count_dict[counts].sort()
            
    return count_dict