def is_opposite(s1,s2):
    '''Determines whether two strings are opposite in case'''
    s1_list = []
    s2_list = []
    if s1 == '':
        return False
    
    for letter in s1:
        if letter.isupper():
            s1_list.append(True)
        else:
            s1_list.append(False)
            
    for letter in s2:
        print(letter)
        if letter.isupper():
            s2_list.append(False)
        else:
            s2_list.append(True)
    print(s1_list)
    print(s2_list)
    
    if s1_list == s2_list:
        return True
        
    else: 
        return False