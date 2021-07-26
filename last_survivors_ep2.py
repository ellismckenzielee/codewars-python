#Last Survivors Ep.2 kata
#https://www.codewars.com/kata/60a1aac7d5a5fc0046c89651

import re
def last_survivors(string):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    pattern = re.compile('([a-z])\\1')
    while True:
        string = ''.join(sorted(string))
        prev = string
        lst_string = list(string)
        matches = re.finditer(pattern, string, flags=0)
        for match in matches:
            start, finish = match.span()
            letter = match.group()[0]
            new_letter = alph[(alph.index(letter) + 1) % 26]
            lst_string[start:finish] = ['PLCHOLDER', 'PLCHOLDER']
            lst_string[start] = new_letter
        lst_string = list(filter(lambda x: x != 'PLCHOLDER', lst_string))
        string = ''.join(lst_string)
        if string == prev:
            return string
