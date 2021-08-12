#pillow on the fridge kata
#https://www.codewars.com/kata/57d147bcc98a521016000320

def pillow(s):
    fridge = 'n' in s[0]
    pillow = 'B' in s[1]
    
    if (pillow == False) or (fridge == False):
        return False
    fridge_index = [i for i, x in enumerate(s[0]) if x == "n"][0]
    pillow_index = [i for i, x in enumerate(s[1]) if x == "B"][-1]

    return fridge_index <= pillow_index

    
    