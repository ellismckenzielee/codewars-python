#plenty of fish in the pond kata
#https://www.codewars.com/kata/5904be220881cb68be00007d

def fish(shoal):
    shoal = sorted(list(map(int, shoal)))
    current_size = 1
    amount_needed = 4
    initial_amount_needed = amount_needed
    
    for fish in shoal:
        if fish <= current_size:
            amount_needed -= fish
            if amount_needed <= 0:
                remainder = abs(amount_needed)
                initial_amount_needed += 4
                amount_needed = initial_amount_needed - remainder
                current_size += 1
        else:
            break
    return current_size

    