# All Start Coding Challenge #15
# https://www.codewars.com/kata/586560a639c5ab3a260000f3/train/python

def rotate(str_):
    rotations = []
    for i in range(len(str_)):
        str_ =  str_[1:] + str_[0:1]
        rotations.append(str_)
    return rotations
        
