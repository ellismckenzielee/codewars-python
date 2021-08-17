#the lamp: revisited kata
#https://www.codewars.com/kata/570e6e32de4dc8a8340016dd

class Lamp:
    def __init__(self, color='red', on=False):
        self.color = color
        self.on = on
        
    def toggle_switch(self):
        if self.on == True:
            self.on = False
        else:
            self.on = True
    
    def state(self):
        if self.on == True:
            return 'The lamp is on.'
        else:
            return 'The lamp is off.'