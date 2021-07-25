#One is the loneliest number kata
#https://www.codewars.com/kata/5dfa33aacec189000f25e9a9

def loneliest(number): 
    diction = {1:1000}
    numbers = list(map(int, list(str(number))))
    loneliest_number = 100
    for i, num in enumerate(numbers):
        if i < num:
            LHS = numbers[:i]
        else:
            LHS = numbers[i-num:i]
        RHS = numbers[i+1: i +1 + num]
        total = sum(LHS) + sum(RHS)
        if num not in diction.keys():
            diction[num] = total
        elif total < diction[num]:
            diction[num] = total
        if total < loneliest_number:
            loneliest_number = total
    
    return True if diction[1] == loneliest_number else False
        
            