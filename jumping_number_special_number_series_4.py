#jumping number (special numbers series #4) kata
#https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed

def jumping_number(number):
    number = list(str(number))
    for i in range(0, len(number)-1):
        if abs(int(number[i+1])-int(number[i])) != 1:
            return 'Not!!'
    return 'Jumping!!'
            