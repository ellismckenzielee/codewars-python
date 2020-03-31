###Range of Integers in Unsorted String - codewars kata
###https://www.codewars.com/kata/5b6b67a5ecd0979e5b00000e

def number_builder(digits, number, s):
    number = str(number)
    for digit in number:
        if str(digit) in digits:
            digits.remove(digit)
        else:
            return False
    return digits
        

def mystery_range(s,n):
    '''Sorts a string of disorganised integers and returns 
    a list of these'''
    all_digits = sorted(list(s))
    nums = []
    i = 0
    starting_num = 200
    while i < 201:
        i += 1
        digits = list.copy(all_digits)
        found_nums = 0
        for num in range(starting_num, starting_num-n, -1):
            response = number_builder(digits, str(num), s)
            if response == False:
                break
            else:
                if str(num) in s:
                    found_nums +=1
                else:
                    break
            if found_nums == n:
                return [num, num + n - 1]
        starting_num -= 1
            
            