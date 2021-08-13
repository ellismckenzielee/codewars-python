#santa's naughty list kata
#https://www.codewars.com/kata/5a0b4dc2ffe75f72f70000ef

def find_children(santas_list, children):
    return sorted(set([child for child in children if child in santas_list]))