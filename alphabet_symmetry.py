#Alphabet Symmetry kata
#https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0

def solve(arr):
    output = []
    for str in arr:
        str = list(map(lambda x: ord(x.lower())-96, list(str)))
        str = list(map(lambda x: x[0] == x[1], zip(str, range(1,len(str)+1))))
        output.append(str.count(True))
    return output
        