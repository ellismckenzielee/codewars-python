def pig_it(text):
    '''Converts text into pig-latin'''
    split_text = text.split(' ')
    pig_sentence = ' '
    
    for word in split_text:
        if word in '!.%&?':
            pig_sentence = pig_sentence + word
        else:
            pig_word = word[1:] + word[0] + 'ay'
            pig_sentence = pig_sentence + pig_word + ' '
    
    
    return pig_sentence.strip(' ') 