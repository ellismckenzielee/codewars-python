#remove duplicate words kata
#https://www.codewars.com/kata/5b39e3772ae7545f650000fc

def remove_duplicate_words(s):
    s = s.split(' ')
    words_used = set()
    output = []
    for word in s:
        print(word)
        if word not in words_used:
            output.append(word)
            words_used.add(word)
    return ' '.join(output)