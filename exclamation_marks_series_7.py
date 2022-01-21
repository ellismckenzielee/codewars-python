##exclamation marks series #7: remove words from the sentence if it 
##contains one exclamation mark
##https://www.codewars.com/kata/57fafb6d2b5314c839000195

def remove(s):
    return ' '.join(filter(lambda word: word.count('!') != 1, s.split(' ')))