## Perform operation to make string empty kata
## https://www.codewars.com/kata/65d2460f512ea70058594a3d

def last_non_empty_string(strng: str) -> str:
    letters = {}
    longest_length = 0
    for index, letter in enumerate(strng):
        if letter not in letters:
            letters[letter] = []
            letters[letter].append(index)
        else:
            letters[letter].append(index)
        if len(letters[letter]) > longest_length:
            longest_length = len(letters[letter])
    word = []
    positions = {}
    for letter, indeces in letters.items():
        if len(indeces) == longest_length:
            position = indeces[-1]
            positions[position] = letter
    output = ""
    for position in sorted(list(positions.keys())):
        output += positions[position]
    return output
            
