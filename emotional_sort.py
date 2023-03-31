# Emotional Sort kata
# https://www.codewars.com/kata/5a86073fb17101e453000258/train/python

def sort_by_face(face):
    faces = [ ':D', ':)', ':|', ':(', 'T_T' ]
    return faces.index(face)

def sort_emotions(arr, order):
    arr.sort(key = sort_by_face, reverse = not order)
    return arr
