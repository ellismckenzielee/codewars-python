#complete the pattern #1 kata
#https://www.codewars.com/kata/5572f7c346eb58ae9c000047

def pattern(n):
    output = ''
    for num in range(1,n+1):
        output += str(num)*num + '\n'
    return output[:-1]
        