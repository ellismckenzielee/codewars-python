###Delete occurrences of an element if it occurs more than n times'''
###https://www.codewars.com/kata/554ca54ffa7d91b236000023

def delete_nth(order,max_e):
    '''Removes elements from order if they have appeared more
    than max_e times'''
    dictionary = {}
    output = []
    for num in order:
        if num in dictionary.keys():
            dictionary[num] += 1
            if dictionary[num] <= max_e:
                output.append(num)
        else:
            dictionary[num] = 1
            output.append(num)
    return output
            