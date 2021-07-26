#Fizzbuzz Backwards kata
#https://www.codewars.com/kata/59ad13d5589d2a1d84000020

def reverse_fizz_buzz(array):
    if 'Fizz' in array:
        fizz = array.index('Fizz')
    else:
        fizz = array.index('FizzBuzz')
    if 'Buzz' in array:
        buzz = array.index('Buzz')
    else:
        buzz = array.index('FizzBuzz')
    
    return (fizz + 1, buzz +1 )