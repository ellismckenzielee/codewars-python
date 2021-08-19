#reversed words kata
#https://www.codewars.com/kata/51c8991dee245d7ddf00000e

def reverseWords(str):
    return (' '.join(str.split(' ')[::-1]))