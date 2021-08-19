#disarium number (special numbers series #3) kata
#https://www.codewars.com/kata/5a53a17bfd56cb9c14000003

def disarium_number(number):
    number_string = str(number)
    total = 0
    for i, num in enumerate(number_string):
        total += int(num)**(i+1)
    return 'Disarium !!' if total == number else 'Not !!'