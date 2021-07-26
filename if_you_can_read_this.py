#If your can read this... kata
#https://www.codewars.com/kata/586538146b56991861000293

def to_nato(words):
    telephony = {
        'a':'Alfa',
        'b':'Bravo',
        'c':'Charlie',
        'd':'Delta',
        'e':'Echo',
        'f':'Foxtrot',
        'g':'Golf',
        'h':'Hotel',
        'i':'India',
        'j':'Juliett',
        'k':'Kilo',
        'l':'Lima',
        'm':'Mike',
        'n':'November',
        'o':'Oscar',
        'p':'Papa',
        'q':'Quebec',
        'r':'Romeo',
        's':'Sierra',
        't':'Tango',
        'u':'Uniform',
        'v':'Victor',
        'w':'Whiskey',
        'x':'Xray',
        'y':'Yankee',
        'z':'Zulu'}
    output = '' 
    for char in words.lower():
        if char == ' ':
            continue
        output += ' '
        if char in telephony.keys():
            output += telephony[char]
        else:
            output += char
    return output.strip()