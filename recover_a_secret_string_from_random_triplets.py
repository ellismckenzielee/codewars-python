#Recover a secret string from random triplets kata
#https://www.codewars.com/kata/53f40dff5f9d31b813000774

def recoverSecret(triplets):
    dict = {}
    for triplet in triplets:
        for j, letter in enumerate(triplet):
            if letter not in dict.keys():
                dict[letter] = []
            dict[letter] += triplet[j+1:]
    output = list(dict.keys())
    sorted_chars = []
    for i in range(0, 5):
        for letter in list(dict.keys()):
            indx = output.index(letter)
            LHS = output[:indx]
            for p, itm in enumerate(LHS):
                if itm in dict[letter]:
                    output.insert(p, letter)
                    del output[indx+1]
                    break
    return ''.join(output)