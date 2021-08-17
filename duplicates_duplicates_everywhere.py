#duplicates, duplicates everywhere kata
#https://www.codewars.com/kata/5e8dd197c122f6001a8637ca/solutions/python

def remove_duplicate_ids(obj):
    letters_used = set()
    for key, lst in sorted(obj.items(), key=lambda x: -int(x[0])):
        new_lst = []
        for letter in lst:
            if letter not in letters_used:
                new_lst.append(letter)
            letters_used.add(letter)
        obj[key] = new_lst
    return obj
        