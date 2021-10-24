#identify ball bearings kata    
#https://www.codewars.com/kata/61711668cfcc35003253180d

def identify_bb(bearings, weigh):
    deluxe, normal, total = 11, 10, 0 
    bearings_selection = []
    for i in range(0, len(bearings)):
        for j in range(0, i+1):
            total += 10
            bearings_selection.append(bearings[i])
    return bearings[(weigh(*bearings_selection) - total - 1)]