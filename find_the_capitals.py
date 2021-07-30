#find the capitals kata
#https://www.codewars.com/kata/53573877d5493b4d6e00050c

def capital(capitals): 
    sentences = []
    for capital in capitals:
        if 'state' in capital.keys():
            type = 'state'
        else:
            type = 'country'
        sentences.append('The capital of {} is {}'.format(capital[type], capital['capital']))
  
    return sentences