#love vs friendship kata
#https://www.codewars.com/kata/59706036f6e5d1e22d000016

def words_to_marks(s):
    return sum(list(map(lambda x: 'abcdefghijklmnopqrstuvwxyz'.index(x) + 1, s)))