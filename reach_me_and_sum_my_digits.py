# reach me and sum my digits kata
# https://www.codewars.com/kata/55ffb44050558fdb200000a4

def sum_dig_nth_term(init_val, pattern_l, nth_term):
    current_term, current_val, counter = 1, init_val, 0
    while current_term < nth_term:
        current_val += pattern_l[counter % len(pattern_l)]
        counter += 1 
        current_term += 1
    return sum(int(digit) for digit in str(current_val))
