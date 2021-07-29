#bases everywhere kata
#https://www.codewars.com/kata/5f47e79e18330d001a195b55

def base_finder(seq):
    sorted_seq = sorted(list(map(lambda x: int(x), seq)))
    sorted_seq = list(map(lambda x: x % 10, sorted_seq))
    return max(sorted_seq) + 1