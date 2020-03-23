###Duplicate Encoder - codewars kata
###https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

def duplicate_encode(word):
    '''Return a new string where items in word are replaced by 
    either a ( or a ) depending on whether more than one exists
    in word'''
    word = list(map(lambda x: x.lower(), word))
    unique = set(word)
    unique_counts = {}
    for elem in unique:
        unique_counts[elem] = word.count(elem)
      
    output = ""
    for elem in word:
        if unique_counts[elem] < 2:
            output += '('
        else:
            output += ')'
    return output