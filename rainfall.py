###This returns the average rainfall and rainfall variance from different datasets (strings)
###See Rainfaill 5Kyu kata for more information on the format of the dataset 
import re
def mean(town, strng):
    data_split = re.findall(r'.+(?:\n|$)', strng)
    for counter, town_info in enumerate(data_split):
        if town in town_info:    
            town_name = re.match(r'\w+', town_info)
            if town != town_name.group():
                continue
            numbers = re.findall(r'\d+\.?\d+', town_info)
            float_numbers = [float(x) for x in numbers]
            return sum(float_numbers)/len(float_numbers)
    return -1
    
def variance(town, strng):
    data_split = re.findall(r'.+(?:\n|$)', strng)
    for counter, town_info in enumerate(data_split):
        if town in town_info:
            town_name = re.match(r'\w+', town_info)
            if town != town_name.group():
                continue
            numbers = re.findall(r'\d+\.?\d+', town_info)
            float_numbers = [float(x) for x in numbers]
            mean = sum(float_numbers)/len(float_numbers)
            squared_nums = [(x-mean)**2 for x in float_numbers]
            return sum(squared_nums)/(len(squared_nums))
    return -1