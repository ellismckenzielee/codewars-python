###Ahh, grabscrab! - codewars kata
###https://www.codewars.com/kata/52b305bec65ea40fe90007a7

def grabscrab(word, possible_words):
    '''Returns all the words in possible words that the pirate 
    might have meant, based upon word'''
    word_sorted = sorted(word)
    return [word for word in possible_words if sorted(word) == word_sorted]