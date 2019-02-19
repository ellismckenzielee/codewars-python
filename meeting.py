import re
def meeting(s):
    '''Organise a list of people at a meeting, in alphabetical order, by their lastname'''
    match = re.findall(r'\w+:\w+', s)
    lastnames = []
    names = {}
    for mat in match:
        lastname = re.findall(r':\w+', mat)[0][1:].upper()
        firstname = re.findall(r'\w+:',mat)[0][:-1].upper()
        print('firstname', firstname)
        print('lastname', lastname)
        
        if lastname in lastnames:
            print(True)
            names[lastname].append(firstname.upper())
            names[lastname] = sorted(names[lastname])
        else: 
            names[lastname] = [firstname]
            lastnames.append(lastname)
    
    sorted_lastnames = sorted(lastnames)
    
    output_names = ''
    for name in sorted_lastnames:
        if len(names[name]) == 1:
            output_names = output_names + ('('+str(name)+', ' +  str(names[name][0]) + ')')
        elif len(names[name]) >1:
            for i in range(0, len(names[name])):
                output_names