###Separate the wheat_from_chaff - codewars kata
###https://www.codewars.com/kata/5bdcd20478d24e664d00002c

def wheat_from_chaff(values):
    number_of_chaff = list(map(lambda x: x< 0, values)).count(True)
    print(number_of_chaff)
    chaff = values[:number_of_chaff]
    wheat = values[number_of_chaff:]
    switchable_chaff = [i for i, x in enumerate(wheat) if x < 0][::-1]
    for i, num in enumerate(chaff):
        if num > 0:
            chaff[i] = wheat[switchable_chaff[0]]
            wheat[switchable_chaff[0]] = num
            del switchable_chaff[0]
            
        #print('CHAFF', chaff)
        #print('WHEAT', wheat)
    return chaff + wheat