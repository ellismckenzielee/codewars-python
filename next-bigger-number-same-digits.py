def next_bigger(n):
    '''Takes a number in string format and returns the next biggest number using the same digits'''
    number_string = str(n)
    number_length = len(number_string)  
    for num in range(1, number_length):
        result = flipper(-(num), -(num+1), number_string)
        print(flipper(-(num), -(num+1), number_string))
        if result > n:
            return minimumchecker(-(num+1),str(result), int(number_string[-(num+1)]))
    return -1
        
def flipper(i,j, string):
    '''Flipper finds the point at which switching two numbers results in a larger number'''
    output_string = list(string)
    output_string[j] = string[i]
    output_string[i] = string[j]
    output_string = ''.join(map(str, output_string))
    return int(output_string)
    
def minimumchecker(i, string, number):
    '''Switching two numbers does not give the next highest number, so minmum checker does this and returns the solution'''
    start_string = string[:i]
    string_slice = string[i:]
    print('str_slice',string_slice)
    for i in range(0, len(string_slice)):
        previous_value = 10
        if int(string_slice[i]) > number:
            if int(string_slice[i]) < previous_value:
                first_value = list(string_slice[i])
                index = i
                
    for i in range(0, 10):
        for k in range(0, len(string_slice)):
            if (int(string_slice[k]) == i) and (k != index):
                first_value.append(string_slice[k])
    output_string = ''.join(map(str,first_value))
    return int(start_string + output_string)