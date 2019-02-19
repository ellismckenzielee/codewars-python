def ordered_count(input):
    '''Counts the number of occurences of each character and returns in tuple format'''
    characters = ''
    counts = []
    
    for letter in input:
        if letter in characters:
            location = characters.find(letter)
            counts[location] = counts[location] + 1
        else:
            characters += letter
            counts.append(1)
    
    output = []
    for i in range(0, len(characters)):
        output.append((characters[i], counts[i]))
        
    return output