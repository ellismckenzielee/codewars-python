#Find the divisors! kata
#https://www.codewars.com/kata/544aed4c4a30184e960010f4

def divisors(integer):
    divisor_list =  [num for num in range(2,integer) if integer % num == 0 ]
    return divisor_list if divisor_list != [] else '{} is prime'.format(integer)