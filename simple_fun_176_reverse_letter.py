#simple fun #176: reverse letter kata
#https://www.codewars.com/kata/58b8c94b7df3f116eb00005b

def reverse_letter(string):
    return ''.join(list(map(lambda x: x if x.isalpha() else '', string))[::-1])

    