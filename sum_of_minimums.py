#sum of minimums! kata
#https://www.codewars.com/kata/5d5ee4c35162d9001af7d699

def sum_of_minimums(numbers):
    return sum(list(map(lambda x: sorted(x)[0], numbers)))