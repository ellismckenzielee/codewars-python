#alphabet wars - reinforces massacre kata
#https://www.codewars.com/kata/593e2077edf0d3e2d500002d/solutions/python

def get_blast_indeces(airstrikes, battlefield_size):
    indeces = []
    for i, strike in enumerate(airstrikes):
        if strike == '*':
            indeces += [i-1, i, i+1]
    return list(filter(lambda x: x >= 0 and x < battlefield_size, set(indeces)))
    
def alphabet_war(reinforces, airstrikes):
    battlefield_size = len(reinforces[0])
    
    #SETUP BATTLEFIELD (LAYER SOLDIERS)
    battlefield = [[] for x in range(battlefield_size)]
    for row, layer in enumerate(reinforces):
        for col, letter in enumerate(layer):
            battlefield[col].append(letter)
            
    
    #FIND INDECES OF EACH AIRSTRIKE AND REMOVE SOLDIER FROM POSITION        
    for airstrike in airstrikes: 
        indeces = get_blast_indeces(airstrike, battlefield_size)
        print(indeces)
        for index in indeces:
            if battlefield[index] == ['_']:
                continue
            elif len(battlefield[index]) == 1:
                battlefield[index] = ['_']
            else:
                battlefield[index].pop(0)
    return ''.join(list(map(lambda x: x[0], battlefield)))