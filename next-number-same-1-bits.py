###Basics 08: Find next higher number with same Bits (1's) - codewars kata
###https://www.codewars.com/kata/56bdd0aec5dc03d7780010a5

def next_higher(value):
    '''Returns next number with same number of 1 bits''' 
    initial = bin(value).split('b')[1].count('1')
    current_num = value+1 
    while True:
        number_1s = bin(current_num).split('b')[1].count('1')
        if number_1s == initial:
            return current_num
        current_num += 1