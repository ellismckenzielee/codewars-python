#is there a vowel in there? kata
#https://www.codewars.com/kata/57cff961eca260b71900008f

def is_vow(inp):
    return [chr(num) if chr(num) in 'aeiou' else num for num in inp]