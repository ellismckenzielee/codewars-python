#square every digit kata
#https://www.codewars.com/kata/546e2562b03326a88e000020

def square_digits(num):
    total = ''
    for num in map(int, str(num)):
        total += str(num**2)
    return int(total) 