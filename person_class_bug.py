# Person Class Bug kata
# https://www.codewars.com/kata/513f887e484edf3eb3000001/train/python

class Person():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = f'{first_name} {last_name}'
