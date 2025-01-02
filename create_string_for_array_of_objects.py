# Creating a string for an array of objects from a set of words kata
# https://www.codewars.com/kata/5877786688976801ad000100

import re
def words_to_object(s):
    matches = re.findall(r"[^ ]+ [^ ]+", s)
    dicts = []
    for mtch in matches:
        name, id = mtch.split(" ")
        dicts.append(f"{{name : '{name}', id : '{id}'}}")
    return f"[{', '.join(dicts)}]"
