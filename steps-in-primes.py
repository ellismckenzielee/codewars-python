##STEPS IN PRIMES KATA
##Code below finds the first set of prime numbers within 
##as specified range, that have a step size equal to g

def step(g, m, n):
    prime_list = []
    for num in range(m, n):
        number_prime = isPrime(num)
        prime_list.append(number_prime)
        if number_prime == True:
            if len(prime_list) > g:
                if prime_list[num-g-m] == True:
                    return [num-g, num]
            else:
                previous_prime = num
        
def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        elif i*i > num:
            return True
    return True