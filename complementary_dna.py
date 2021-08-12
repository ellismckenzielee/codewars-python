#complementary DNA kata
#https://www.codewars.com/kata/554e4a2f232cdd87d9000038

def complementary(letter):
    return ['A','T','C','G'][['T','A','G','C'].index(letter)]
    
def DNA_strand(dna):
    return ''.join(list(map(complementary, dna)))