#Almost Even kata
#https://www.codewars.com/kata/529e2e1f16cb0fcccb000a6b

def split_integer(num, parts):
    output = [num // parts for i in range(parts)]
    remainder = num % parts
    if remainder > 0:
        for i in range(remainder):
            output[i] += 1
    return sorted(output)