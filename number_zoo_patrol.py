#Number zoo partrol kata
#https://www.codewars.com/kata/5276c18121e20900c0000235

def find_missing_number(numbers):
    return sum(list(range(1, len(numbers)+2))) - sum(numbers) 