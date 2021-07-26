#Grouped by commas kata
#https://www.codewars.com/kata/5274e122fc75c0943d000148


def group_by_commas(n):
    n = str(n)[::-1]
    output = ''
    for i, num in enumerate(n):
        if (i) % 3 == 0 and i != 0:
            output += ','
        output += num
    return output[::-1]