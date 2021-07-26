#First non-repeating character kata
#https://www.codewars.com/kata/52bc74d4ac05d0945d00054e

def first_non_repeating_letter(string):
    initial_string = [[char, i] for i, char in enumerate(string)]
    string, repeating = list(string.lower()), True
    string = [[char, i] for i, char in enumerate(string)]

    while len(string) >= 1:
        indx = string[0][1]
        char = string[0][0]
        old_len = len(string)
        string = list(filter(lambda x: x[0] != char, string))
        new_len = len(string) + 1
        if new_len == old_len:
            return initial_string[indx][0]
    return ''