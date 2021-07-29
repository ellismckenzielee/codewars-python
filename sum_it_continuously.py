#sum it continuously kata
#https://www.codewars.com/kata/59b44d00bf10a439dd00006f

def add(l):
    output = [0]
    for i in range(len(l)):
        total = l[i] + output[i]
        output.append(total)
    return output[1:]