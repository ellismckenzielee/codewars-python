###Product Array - codewars kata
###https://www.codewars.com/kata/5a905c2157c562994900009d

def product_array(numbers):
    '''Returns an array based on numbers input. At index
    i, the output contains the product of all elements in numbers,
    excluding the element at position i'''
    output = []
    total = numbers[0]
    
    for num in numbers[1:]:
        total *= num
    
    for num in numbers:
        output.append(total/num)
    return output
