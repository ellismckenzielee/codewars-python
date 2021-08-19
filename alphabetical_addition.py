#alphabetical addition kata
#https://www.codewars.com/kata/5d50e3914861a500121e1958

def add_letters(*letters):
    letter_list = list('abcdefghijklmnopqrstuvwxyz')
    new_index = 0
    for letter in letters:
        new_index += (letter_list.index(letter)+1)
    return letter_list[(new_index -1)  % 26]