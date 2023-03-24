# Thue-Morse Sequence kata 
# https://www.codewars.com/kata/591aa1752afcb02fa300002a/train/python

def thue_morse(n,seq ='0'):
    if len(seq) >= n:
        return seq[0:n]
    else:
        return thue_morse(n, seq + complementary(seq))

def complementary(str):
    complement = ''
    for b in str:
        if b == "1":
            complement += '0'
        else:
            complement += '1'
    return complement
