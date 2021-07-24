#first character that repeats kata
#https://www.codewars.com/kata/54f9f4d7c41722304e000bbb


def first_dup(s):    
    for letter in s:
        if s.count(letter) > 1:
            return letter
            