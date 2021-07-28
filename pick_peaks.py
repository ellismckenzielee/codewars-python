#pick peaks kata
#https://www.codewars.com/kata/5279f6fe5ab7f447890006a7

def pick_peaks(arr):
    output = {
        'pos': [],
        'peaks': []
    }
    if not arr:
        return output
    
    condition = 'down'
    previous = [arr[0], 0]
    for i, num in enumerate(arr[1:]):
        if num > previous[0]:
            condition = 'up'
            previous = [num, i+1]
        elif num < previous[0]:
            if condition == 'up':
                output['pos'].append(previous[1])
                output['peaks'].append(previous[0])
            condition = 'down'
            previous = [num, i+1]
        
    return output