#special number (special numbers series #5) kata
#https://www.codewars.com/kata/5a55f04be6be383a50000187

def special_number(number):
    return 'Special!!' if sum([1 if num in ['1','2','3','4','5','0'] else 0 for num in str(number)]) == len(str(number)) else 'NOT!!'