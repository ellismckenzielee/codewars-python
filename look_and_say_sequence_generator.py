# Look and say sequence generator kata
# https://www.codewars.com/kata/592421cb7312c23a990000cf

def look_and_say_sequence(first_element, n):
    if n == 1:
        return first_element
    current_count = 0
    current_char = first_element[0]
    output = ''
    for char in first_element:
        if char == current_char:
            current_count += 1
        else:
            output += f'{current_count}{current_char}'
            current_char, current_count = char, 1
    output += f'{current_count}{current_char}'
    return look_and_say_sequence(output, n - 1)
            
