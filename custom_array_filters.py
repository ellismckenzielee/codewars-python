#custom array filters kata
##https://www.codewars.com/kata/53fc954904a45eda6b00097f

class list:
    def __init__(self, list):
        self.list = [elem for elem in filter(lambda elem: type(elem) == int, list)]

    def even(self):
        self.list = [elem for elem in filter(lambda elem: elem % 2 == 0, self.list)]
        return self.list
    
    def odd(self):
        self.list = [elem for elem in filter(lambda elem: elem % 2 != 0, self.list)]
        return self.list

    def under(self, val):
        self.list = [elem for elem in filter(lambda elem: elem < val != 0, self.list)]
        return self.list

    def over(self, val):
        self.list = [elem for elem in filter(lambda elem: elem > val != 0, self.list)]
        return self.list
    
    def in_range(self, lower, upper):
        self.list = [elem for elem in filter(lambda elem: elem >= lower and elem <= upper != 0, self.list)]
        return self.list