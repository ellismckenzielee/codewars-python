#Split Without Loss kata
#https://www.codewars.com/kata/581951b3704cccfdf30000d2

def split_without_loss(s, split_p):
    strng = split_p
    before, after = strng.split('|')
    strng = ''.join(before + after)
    strng_to_split, i  = '', 0
    while i < len(s):
        if strng not in s[i:i+len(strng)]:
            strng_to_split += s[i]
            i += 1
        else:
            strng_to_split  += before + 'SPLIT' + after
            i += len(strng) 
            
    return strng_to_split.strip('SPLIT').split('SPLIT')