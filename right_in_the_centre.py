#right in the centre kata
#https://www.codewars.com/kata/5f5da7a415fbdc0001ae3c69

def is_in_middle(sequence):
    length = len(sequence)
    central_index = int((length-1)/2)
    for i in range(0, length-2):
        if sequence[i] + sequence[i+1] + sequence[i+2] == 'abc':
            print(i)
            if length % 2 == 0:
                if (central_index >= i) and (central_index < i + 2):
                    return True
            else:
                if (central_index > i) and (central_index < i + 2):
                    return True
    return False