# Van Ecks Sequence kata 
# https://www.codewars.com/kata/62e4df54323f44005c54424c/train/python

def seq(n):
    sequence, head = [0], 0
    while len(sequence) < n:
        head = sequence[0]
        if head not in sequence[1:]:
            sequence = [0] + sequence
        else: 
            distance = sequence[1:].index(head) + 1
            sequence = [distance] + sequence 
    return sequence[0]
    
