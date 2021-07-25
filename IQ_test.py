#IQ Test kata
#https://www.codewars.com/kata/552c028c030765286c00007d

def iq_test(numbers):
    numbers = list(map(int, numbers.split(' ')))
    evens, edx = 0, 0
    odds, odx = 0, 0
    for i, num in enumerate(numbers):
        if num % 2 == 0:
            evens += 1
            edx = i
        else:
            odds += 1
            odx = i
    return [edx, odx][[evens, odds].index(min(evens, odds))] + 1
