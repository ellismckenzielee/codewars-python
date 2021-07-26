#Hells Kitchen kata
#https://www.codewars.com/kata/57d1f36705c186d018000813

def gordon(a):
    a = ' '.join(list(map(lambda x: x.upper()+'!!!!', a.split(' '))))
    for letter in 'AEIOU':
        if letter == 'A':
            replacement = '@'
        else:
            replacement = '*'
        a = a.replace(letter, replacement)
    return a
    
