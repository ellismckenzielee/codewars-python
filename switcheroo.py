#Switcheroo kata
#https://www.codewars.com/kata/57f759bb664021a30300007d

def switcheroo(string):
    return ''.join([char if char =='c' else ['a','b'][1-['a','b'].index(char)] for char in string])