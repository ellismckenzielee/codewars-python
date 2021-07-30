#the vowel code kata
#https://www.codewars.com/kata/53697be005f803751e0015aa

def switcher(char):
    dict1 = {'a':'1','e':'2','i':'3','o':'4','u':'5'}
    dict2 = {'1':'a','2':'e','3':'i','4':'o','5':'u'}

    if char in dict1.keys():
        return dict1[char]
    elif char in dict2.keys():
        return dict2[char]
    return char

def encode(st):
    return ''.join(list(map(switcher, list(st))))
    
def decode(st):
    return ''.join(list(map(switcher, list(st))))