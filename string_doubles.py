#string doubles kata
#https://www.codewars.com/kata/5a145ab08ba9148dd6000094

def doubles(s):
    previous, counter, s = '', 0, list(s)
    while True:
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                s[i], s[i+1] = '0', '0'
                
        output = ''.join(list(filter(lambda x: x != '0', s)))
        if output == previous:
            return output
        else:
            previous = output
            s = list(output)
