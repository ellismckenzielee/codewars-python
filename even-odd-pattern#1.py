###Even Odd Pattern #1
###https://www.codewars.com/kata/559e708e72d342b0c900007b

def even_odd(arr):
    '''Returns a total based on a formula that I had to work out'''
    total = 0
    for i, num in enumerate(arr):
        print(i%2)
        if i % 2 != 0:
            total *= num
        else:
            total += num
    return total 