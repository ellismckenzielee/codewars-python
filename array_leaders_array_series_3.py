#array leaders (array series #3) kata
#https://www.codewars.com/kata/5a651865fd56cb55760000e0

def array_leaders(numbers):
    output = []
    for i in range(0, len(numbers)):
        if numbers[i] > sum(numbers[i+1:]):
            output.append(numbers[i])
    return output