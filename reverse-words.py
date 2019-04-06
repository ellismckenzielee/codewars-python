def reverse_words(text):
    n = text.count(' ')
    if n == 0:
        return text[::-1]
    text_split = text.split()
    spaces = ' '*int((n/(len(text_split) -1)))
    return spaces.join([section[::-1] for section in text_split])