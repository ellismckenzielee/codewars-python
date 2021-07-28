#remove consecutive duplicate words kata
#https://www.codewars.com/kata/5b39e91ee7a2c103300018b3

def remove_consecutive_duplicates(s):
    s = s.split(' ')
    output = [0]
    for  word in s:
        print(word)
        if word != output[-1]:
            output.append(word)
    return ' '.join(output[1:])