#numericals of a string kata
#https://www.codewars.com/kata/5b4070144d7d8bbfe7000001

def numericals(s):
    dict = {
        }
    output_list = []
    for letter in s:
        if letter not in dict.keys():
            dict[letter] = 0
            output_list.append(1)
        else:
            dict[letter] += 1
            output_list.append(dict[letter]+1)
    return ''.join(map(str, output_list)) 