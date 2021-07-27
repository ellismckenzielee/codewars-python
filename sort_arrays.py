#sort arrays - 3 kata
#https://www.codewars.com/kata/51f42b1de8f176db5a0002ae

def sort_me(courses): 
    courses = sorted(courses, key=lambda x: (x.split('-')[1],x.split('-')[0]))
    return courses