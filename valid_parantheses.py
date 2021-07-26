#Valid parantheses kata
#https://www.codewars.com/kata/52774a314c2333f0a7000688

def valid_parentheses(string):
    count = 0
    for char in string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0