import numpy as np
def sum_pairs(ints, s):
    '''First attempt as sum-pairs. Code timed out'''
    index = 0
    
    possibles = []
    possibles_final_indeces = [] 
    previous_num = 132352
    
    for num in ints:
        if num == previous_num:
            continue
        else: 
            required_num = s - num
            try:
                location = np.where(np.array(ints[index+1:]) == required_num)[0][0] + index +1
                possibles.append([index, location])
                possibles_final_indeces.append(location)
            except:
                pass    
            
            if possibles_final_indeces:
                if index >= possibles_final_indeces[0]:
                    break
          
        index=index+1
        previous_num = num
    
    if possibles_final_indeces != []:
        correct_val_location = np.where(possibles_final_indeces == np.min(possibles_final_indeces))[0][0]
        
    if possibles:
        return [ints[possibles[correct_val_location][0]], ints[possibles[correct_val_location][1]]]