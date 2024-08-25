# excel COUNTIF, SUMIF and AVERAGEIF functions kata
# https://www.codewars.com/kata/56055244356dc5c45c00001e
import re
def greater_than(a,b):
    return a > b

def greater_than_or_equal_to(a,b):
    return a >= b

def less_than(a,b):
    return a < b

def less_than_or_equal_to(a,b):
    return a <= b

def not_equal_to(a,b):
    return a != b

def equals(a, b):
    return a == b 

def convert_criteria_to_func(criteria):
    NOT = re.compile("<>[\-0-9]")
    GT = re.compile(">[\-0-9]")
    GTE = re.compile(">=[\-0-9]")
    LT = re.compile("<[\-0-9]")
    LTE = re.compile("<=[\-0-9]")
    
    func = greater_than
    if re.match(GT, criteria):
        func = greater_than
    elif re.match(GTE, criteria):
        func = greater_than_or_equal_to
    elif re.match(LT, criteria):
        func = less_than
    elif re.match(LTE, criteria):
        func = less_than_or_equal_to
    elif re.match(NOT, criteria):
        func = not_equal_to
    return func
            
def handle_criteria(func):
    def inner_func(values, criteria):
        if type(criteria) == int:
            b = criteria
            comparison_func = equals
        else:
            num_results = re.findall(r"[\-0-9.]+", criteria)[0]
            b = float(num_results)
            comparison_func = convert_criteria_to_func(criteria)
        filtered_values = list(filter(lambda value: comparison_func(value, b), values))
        return func(filtered_values)  
    return inner_func

@handle_criteria
def count_if(filtered_values):
    return len(filtered_values)
    
@handle_criteria
def sum_if(filtered_values):
    return sum(filtered_values)  

@handle_criteria
def average_if(filtered_values):
    return sum(filtered_values)/len(filtered_values)
