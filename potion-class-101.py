#Codewars Potion Class 101 Kata
#https://www.codewars.com/kata/5981ff1daf72e8747d000091

import math
class Potion:
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume
    
    def mix(self, other):
        self.other = other
        self.other_volume = self.other.volume
        
        #NEW POTION VOLUME
        self.new_volume = self.other_volume + self.volume
        
        #MIXING RATIOS
        x = self.volume/self.new_volume
        y = self.other_volume/self.new_volume

        ###NEW POTION COLORS        
        self.new_color1 =  math.ceil(x*self.color[0] + y*self.other.color[0])
        self.new_color2 =  math.ceil(x*self.color[1] + y*self.other.color[1])
        self.new_color3 =  math.ceil(x*self.color[2] + y*self.other.color[2])
        return Potion((self.new_color1, self.new_color2, self.new_color3), self.new_volume)
        