#simple fun #135: missing alphabets kata
#https://www.codewars.com/kata/58a664bb586e986c940001d5

def missing_alphabets(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    maximum_count = 0
    letter_count = []
    for letter in letters:
        count = s.count(letter)
        if count > maximum_count:
            maximum_count = count
        letter_count.append([letter, count])
    output = ""
    for letter in letter_count:
        output += (letter[0]*(maximum_count-letter[1]))
    return output
    
        