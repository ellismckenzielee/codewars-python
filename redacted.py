#Redacted! kata
#https://www.codewars.com/kata/5b662d286d0db722bd000013

def redacted(doc1, doc2):   
    if len(doc1) != len(doc2):
        return False
    for i, char in enumerate(doc1):
        if (char != doc2[i] and char != 'X') or (char == 'X' and doc2[i] == '\n'):
            return False
    return True
            