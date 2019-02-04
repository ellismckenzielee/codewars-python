def is_prime(num):
    '''Finds whether a number is prime'''
    if num == 0 or num == 1 or num < 0:
        return False
    else:
        for i in range(2, num+1):
            if (num % i == 0 and num != i):
                return False
            elif (num % i == 0) and (num == i):
                return True