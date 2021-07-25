#Pairs of Bears kata
#https://www.codewars.com/kata/57d165ad95497ea150000020

def bears(x,s):
    output = ""
    previous = False
    counts = 0
    for i in range(0, len(s) -1):
        letters = s[i] + s[i+1]
        if (letters == 'B8' or letters == '8B') and previous == False:
            output += letters
            previous = True
            counts += 1
        else:
            previous = False
    return [output,  counts >= x]