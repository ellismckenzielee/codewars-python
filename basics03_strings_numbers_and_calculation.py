#Basics 03: Strings, Numbers and Calculation kata
#https://www.codewars.com/kata/56b5dc75d362eac53d000bc8

import re
def find_op(char):
    if char in ['/', '+', '-', '*']:
        return char 
        
def calculate(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '/':
        return num1 / num2
    elif op == '*':
        return num1 * num2
    elif op == '-':
        return num1 - num2
        
def calculate_string(st): 
    matches = re.findall('[0-9\+\-\*\/\.]+', st)
    operator = list(filter(find_op, st))[0]
    matches = ''.join(matches)
    num1, num2 = matches.split(operator)


    return str(int(round(calculate(float(num1),float(num2), operator))))
    