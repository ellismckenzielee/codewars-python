#detect pangram kata
#https://www.codewars.com/kata/545cedaa9943f7fe7b000048

def is_pangram(s):
    return len(set(filter(lambda x: x.isalpha(),s.lower()))) == 26