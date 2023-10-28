# Popping Blocks kata
# https://www.codewars.com/kata/651bfcbcdb0e8b104175b97e/train/python

def pop_blocks(lst):
    if len(lst) <= 1:
        return lst
    found_chain, indexes_to_remove = False, set()
    for i in range(len(lst)-1):
        block_1 = lst[i]
        block_2 = lst[i+1]
        if block_1 == block_2:
            found_chain = True
            indexes_to_remove.add(i)
            indexes_to_remove.add(i+1)
        elif found_chain:
            break
    new_lst = [elem for i, elem in enumerate(lst) if i not in indexes_to_remove]
    return pop_blocks(new_lst) if len(new_lst) != len(lst) else lst

            
        
