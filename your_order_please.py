#Your order, please kata
#https://www.codewars.com/kata/55c45be3b2079eccff00010f

def order(sentence):
    words = sentence.split(' ')
    output = ['' for word in words]
    for word in words:
        for char in word:
            if char in '123456789':
                output[int(char)-1] = word
    return ' '.join(output)