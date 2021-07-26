#Message Validator kata
#https://www.codewars.com/kata/5fc7d2d2682ff3000e1a3fbc

import re
def is_a_valid_message(message):
    if message == "":
        return True
    elif message == [] or not message[0].isnumeric():
        return False

    matches = re.findall(r"([0-9]+)([a-zA-Z]+|$)", message)
    for match in matches:
        if len(match[1]) != int(match[0]):
            return False
    return True
