#Sum consecutives kata
#https://www.codewars.com/kata/55eeddff3f64c954c2000059

def sum_consecutives(s):
    output = []
    previous = s[0]
    total = s[0]
    for num in s[1:]:
        if num == previous:
            total += num
        else:    
            output.append(total)
            total = num
            previous = num
    output.append(total)
    return output