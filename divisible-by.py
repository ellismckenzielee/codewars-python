def divisible_by(numbers, divisor):
    '''Return numbers in numbers list divisible by the divisor'''
    return [x for x in numbers if (x % divisor == 0)]