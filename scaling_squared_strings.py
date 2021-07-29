#scaling squared strings kata
#https://www.codewars.com/kata/56ed20a2c4e5d69155000301

def scale(strng, k, v):
    output = ''
    substrings = strng.split('\n')
    for sub in substrings:
        temp = ''
        for char in sub:
            temp += char * k
            print(temp)
        output += (temp +'\n') * v
        temp = ''
    return output.strip('\n')