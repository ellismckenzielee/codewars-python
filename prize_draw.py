## Prize Draw kata
## https://www.codewars.com/kata/5616868c81a0f281e500005c

def getWeight(name, weighting):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    weight = 0
    for letter in name.lower():
        print(letter, alphabet.index(letter))
        weight += alphabet.index(letter) + 1
    return {'name': name, 'weight': (weight + len(name))*weighting}

def rank(st, we, n):
    names = st.split(',')
    if len(st) == 0:
        return 'No participants'
    if len(names) < n:
        return 'Not enough participants'
    weightings = sorted(list(map(getWeight, names, we)), key=lambda score_obj: (-score_obj['weight'], score_obj['name']))
    return weightings[n-1]['name']
    
    