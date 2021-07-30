#interview question (easy) kata
#https://www.codewars.com/kata/5b358a1e228d316283001892

def get_strings(city):
    city = city.lower()
    output = ''
    letters_considered = set()
    for letter in city:
        if letter not in letters_considered and letter.isalnum():
            output += letter + ':' + '*'*city.count(letter) +','
            letters_considered.add(letter)
    return output[:-1]