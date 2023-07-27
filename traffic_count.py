# Traffic Count During Peak Hours kata
# https://www.codewars.com/kata/586ed2dbaa0428f791000885/train/python

def traffic_count(array):
    hours = [('4:00pm', 0), ('5:00pm', 1), ('6:00pm', 2), ('7:00pm', 3)]
    traffic = [(hour, max(array[hour_indx*6:(hour_indx*6)+6])) for hour, hour_indx in hours]
    return traffic
