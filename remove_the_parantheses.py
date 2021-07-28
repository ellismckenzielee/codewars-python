#remove the parantheses kata
#https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8

def remove_parentheses(s):
    output = ''
    current_level = 0
    for char in s:
        print(char)
        if char not in '()':
            if current_level == 0:
                output += char
        else: 
            if char == '(':
                print(True)
                current_level +=1
            elif char == ')':
                current_level -= 1
    return output
            