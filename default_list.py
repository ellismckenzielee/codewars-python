###DefaultList - codewars kata
###https://www.codewars.com/kata/5e882048999e6c0023412908
###See link for details

class DefaultList:
    def __init__(self, list, default):
        self.list = list
        self.default = default
        
    def check_index(self, val):
        if  val < -len(self.list) or val >= len(self.list):
            return False
        else:
            return True
            
    def __getitem__(self, val):
        if not self.list:
            return self.default
        return self.list[val] if self.check_index(val) == True else self.default   
    
    def extend(self, extend_list):
        self.list = self.list + extend_list
    
    def append(self, append_list):
        self.list.append(append_list)
      
    def remove(self, char):
        if char in self.list:
            self.list.remove(char)
        
    def insert(self, index, new_val):        
        self.list.insert(index, new_val)
        
    def pop(self, index):
        if  self.check_index(index) == False:
            return self.default
        else:
            del self.list[index]