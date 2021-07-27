#javascript array filter kata
#https://www.codewars.com/kata/514a6336889283a3d2000001

def get_even_numbers(arr):
    return list(filter(lambda x: x%2 == 0, arr)) 