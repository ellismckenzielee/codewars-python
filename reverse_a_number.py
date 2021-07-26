#Reverse a number kata
#https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5

def reverse_number(n):
    n, flag = str(n), 1
    if n[0] == '-':
        flag = -1
        n = n[1:]
    return flag*int(str(n)[::-1])