#running out of space kata
#https://www.codewars.com/kata/56576f82ab83ee8268000059

def spacey(array):
    output = []
    combined = ''
    for word in array:
        combined += word
        output.append(combined)
    return output
        