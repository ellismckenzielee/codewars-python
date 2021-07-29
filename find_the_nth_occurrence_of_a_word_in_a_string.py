#find the nth occurrence of a word in a string! kata
#https://www.codewars.com/kata/5b1d1812b6989d61bd00004f

def find_nth_occurrence(substring, string, occurrence=0):
    count = 0
    for i, char in enumerate(string):
        captured_string = string[i: i+len(substring)]
        if captured_string == substring:
            count +=1
            if count == occurrence:
                return i
    return -1
            