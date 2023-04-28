# Simple Fun #156: Rotate Paper by 180 Degrees kata
# https://www.codewars.com/kata/58ad230ce0201e17080001c5/train/python

mapping = {
    '2': '2',
    '5': '5',
    '6': '9',
    '8': '8',
    '9': '6', 
    '0': '0'
}
def rotate_paper(numbers):
    reversed_numbers = ''
    mapping_keys = mapping.keys()
    for num in list(numbers):
        if num not in mapping_keys:
            return False
        else:
            reversed_numbers += mapping[num]
    return reversed_numbers[::-1] == numbers
        
