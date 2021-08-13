#tail swap kata 
#https://www.codewars.com/kata/5868812b15f0057e05000001

def tail_swap(strings):
    split_1 = strings[0].split(':')
    split_2 = strings[1].split(':')
    return [split_1[0]+':'+split_2[1],split_2[0]+':'+split_1[1]] 