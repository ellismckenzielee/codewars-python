#unique digits sequence kata
#https://www.codewars.com/kata/599688d0e2800dda4e0001b0

def find_num(n):
    sequence = ['1']
    numbers_considered = set([0,1])
    condition = False
    current_number = 2
    i = 1
    
    if n == 1:
        return 1
    
    while condition == False:
        digits = list(sequence[-1])
        current_number_digits = list(str(current_number))
        check =  any(item in current_number_digits for item in digits)
        if check == True or str(current_number) in sequence:
            numbers_considered.add(current_number)
            current_number += 1
            
        else:
            if str(current_number) not in sequence:
                sequence.append(str(current_number))
                current_number = 1
                
        if len(sequence) >= n:
            condition = True
      
    return int(sequence[-1])        