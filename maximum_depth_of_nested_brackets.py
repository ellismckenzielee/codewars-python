#Maximum Depth of Nested Brackets kata
#https://www.codewars.com/kata/60e4dfc1dc28e70049e2cb9d

def strings_in_max_depth(s):
    order, max_depth = 0, 0
    sub_string = []
    str = ''
    for i, char in enumerate(s):
        if char =='(':
            str = ''
            order += 1
        elif char == ')' and order > 0:
            sub_string.append([order, str])
            order -=1
            str = '' 
        else:
            str += char
        if order > max_depth:
            max_depth = order
    if max_depth == 0:
        return [s]
    else:
        return list(map(lambda x: x[1], (filter(lambda x: x[0] == max_depth, sub_string))))