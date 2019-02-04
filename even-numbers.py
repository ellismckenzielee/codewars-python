def even_numbers(arr,n):
    '''Returns the last n numbers of a list of even numbers from array arr'''
    output = []
    for num in arr:
        if num % 2 == 0:
            output.append(num)
    return output[-n:]