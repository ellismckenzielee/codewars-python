#split and then add both sides of an array together kata
#https://www.codewars.com/kata/5946a0a64a2c5b596500019a

def split_and_add(numbers, n):
    while n > 0:
        split_index = int(len(numbers)/2)
        lhs_list = numbers[:split_index]
        rhs_list = numbers[split_index:]
        if len(lhs_list) < len(rhs_list):
            lhs_list.insert(0, 0)
        zipped_list = list(zip(lhs_list, rhs_list))
        numbers = list(map(sum, zipped_list))
        n -= 1
    return numbers