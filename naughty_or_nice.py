#naughty or nice? kata
#https://www.codewars.com/kata/52a6b34e43c2484ac10000cd

def return_names(people,nice=True):
    output = []
    for person in people:
        if (person['was_nice'] == True) and (nice==True):
            output.append(person['name'])
        elif (person['was_nice'] == False) and (nice==False):
            output.append(person['name'])
    return output
def get_nice_names(people):
    return return_names(people)
    
def get_naughty_names(people):
    return return_names(people, False)