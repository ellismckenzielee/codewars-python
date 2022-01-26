## Packet Delivery - Enforcing Constraints kata
## https://www.codewars.com/kata/587e1ef6f1a2534bbe0001ef

class DimensionsOutOfBoundError(Exception):
    def __init__(self, type, value, lim1, lim2):
        self.type = type
        self.value = value
        super().__init__(f'Package {type}=={value} out of bounds, should be: {lim1} < {type} <= {lim2}')
        
        
class Package(object):
    def __init__(self, length, width, height, weight):
        self.length= length
        self.width= width
        self.height= height
        self.weight= weight

        
    @property    
    def length(self):
        return self._length
        
    @length.setter
    def length(self, length):
        if length < 0 or length > 350:
            raise DimensionsOutOfBoundError('length', length, 0, 350)
        else:
            self._length = length
    
    @property
    def width(self):
        return self._width
          
    @width.setter
    def width(self, width):
        if width < 0 or width > 300:
            raise DimensionsOutOfBoundError('width', width, 0, 300)
        else:
            self._width = width
            
    @property  
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        if height < 0 or height > 150:
            raise DimensionsOutOfBoundError('height', height, 0, 150)
        else:
            self._height = height

    @property
    def weight(self):
        return self._weight
        
    @weight.setter
    def weight(self, weight):
        if weight < 0 or weight > 40:
            raise DimensionsOutOfBoundError('weight', weight, 0, 40)
        else:
            self._weight = weight
    @property
    def volume(self):
        return self.length * self.width * self.height
        
        