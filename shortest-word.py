def find_short(s):
    '''Return the length of the shortest word in a string of words'''
    words = s.split(" ")
    l = len(words[0])
    for word in words:
        if len(word) < l:
            l = len(word)
            print(l)
    return l # l: shortest word length