#increment with iterations kata
#https://www.codewars.com/kata/5ecc16daa200d2000165c5b1

def increment(number, iterations, spacer):
    i = 0
    increment = spacer
    length = len(str(number))   
    while i < iterations:
        str_num = str(number)
        index = spacer % length
        i += 1
        num = int(str_num[index])
        number += 10**(length - index-1)
        new_str_num = str(number)
        if len(new_str_num) > len(str_num):
            length = len(new_str_num)
            spacer = index + 1 
        
        spacer += increment
        
    return number
