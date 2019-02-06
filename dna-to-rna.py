def DNAtoRNA(dna):
    '''Convert DNA to RNA by switching T to U'''
    return ''.join(list(map(tTou, dna)))
    
def tTou(letter):
    if letter == 'T':
        return 'U'
    else:
        return letter