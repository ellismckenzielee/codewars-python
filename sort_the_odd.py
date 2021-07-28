#sort the odd kata
#https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

def sort_array(source_array):
    odds = []
    for i, num in enumerate(source_array):
        if num % 2 != 0:
            odds.append(num)
            source_array[i] = None
    output = []
    for num in sorted(odds):
        index = source_array.index(None)
        source_array[index] = num
    return source_array
    