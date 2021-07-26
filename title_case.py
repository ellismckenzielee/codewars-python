#Title Case kata
#https://www.codewars.com/kata/5202ef17a402dd033c000009

def title_case(title, minor_words=''):
    title = title.split(' ')
    minor_words = minor_words.split(' ')
    minor_words = list(map(lambda x: x.lower(), minor_words))
    output = title[0].title()
    for word in title[1:]:
        if word.lower() not in minor_words:
            output += ' ' + word.title()
        else:
            output += ' ' + word.lower()
    return output