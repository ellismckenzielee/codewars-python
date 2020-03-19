###Find all non-consecutive numbers - codewars kata
###https://www.codewars.com/kata/58f8b35fda19c0c79400020f

def all_non_consecutive(arr):
    '''Returns value and index of all non-consecutive numbers.
    A consecutive number is larger than the number at the previous 
    index by 1'''
    output = []
    for i, num in enumerate(arr[1:]):
        if num != (arr[i]+1):
            output.append({'n': num, 'i': i+1})
    return output
    