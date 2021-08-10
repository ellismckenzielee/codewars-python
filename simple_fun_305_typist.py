#simple fun #305: typist kata
#https://www.codewars.com/kata/592645498270ccd7950000b4/solutions/python


def check_case(char):
    if char.isupper():
        return True
    return False

def typist(s):
    upper, output = False, 0
    for char in s:
        output += 1
        new_case = check_case(char)
        if new_case != upper:
            upper = new_case
            output += 1
    return output
        