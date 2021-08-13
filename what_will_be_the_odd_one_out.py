#what will be the odd one out? kata
#https://www.codewars.com/kata/55b080eabb080cd6f8000035

def odd_one_out(s):
    characters = {}
    checked = set()
    output_list = []
    for i, char in enumerate(s):
        if char not in checked:
            characters[char] = [s.count(char) % 2 == 1, len(s) - 1 - s[::-1].index(char)]
            checked.add(char)
        if characters[char][0] == True and characters[char][1] == i:
            output_list.append(char)
    return output_list
            
            
            