#most valuable character kata
#https://www.codewars.com/kata/5dd5128f16eced000e4c42ba

def solve(st):
    letters_captured = set()
    letters = {}
    ###CREATE DICTIONARY OF EACH ELEMENT IN ST
    ###RECORD MIN AND MAX INDEX
    for i, letter in enumerate(st):
        if letter not in letters_captured:
            letters_captured.add(letter)
            letters[letter] = [i]
        else:
            letter_indeces = letters[letter]
            if len(letter_indeces) <2:
                letter_indeces.append(i)
            else:
                letter_indeces[-1] = i
            letters[letter] = letter_indeces
    
    
    ###SORT DICTIONARY BASED ON INDECES
    previous_valuation = 0
    return_letter = st[0]
    for key, values in letters.items():
        valuation = values[-1] - values[0]
        if valuation > previous_valuation:
            return_letter = key
            previous_valuation = valuation
        elif valuation == previous_valuation:
            if key < return_letter:
                return_letter = key
                previous_valuation = valuation
    
    return return_letter
        