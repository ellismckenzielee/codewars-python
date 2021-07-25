#Death by coffee kata
#https://www.codewars.com/kata/57db78d3b43dfab59c001abe

def coffee_limits(year, month, day):
    CAFE = 51966
    DECAF = 912559
    cafes_allowed = []
    decafs_allowed = []
    year = str(year)
    if month < 10:
        month = '0' + str(month)
    else:
        month = str(month)
    if day < 10:
        print(day)
        day = '0' + str(day)
    else:
        day = str(day)
        
    health_number = int(year+month+day)
    for i in range(1, 5001):
        CAFE_total = health_number + (i*CAFE)
        DECAF_total = health_number + (i*DECAF)
        CAFE_hex_total = hex(CAFE_total)
        DECAF_hex_total = hex(DECAF_total)
        if 'dead' in CAFE_hex_total:
            cafes_allowed.append(i)
        if 'dead' in DECAF_hex_total:
            decafs_allowed.append(i)
    print(cafes_allowed)
    if not cafes_allowed:
        cafes_allowed = 0
    else:
        cafes_allowed = cafes_allowed[0]
    if not decafs_allowed:
        decafs_allowed = 0
    else:
        decafs_allowed = decafs_allowed[0]
    return [cafes_allowed, decafs_allowed]