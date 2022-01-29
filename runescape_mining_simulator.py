## Runescape Mining Simulator kata
## https://www.codewars.com/kata/61b09ce998fa63004dd1b0b4

from preloaded import EXPERIENCE, ROCKS

class Miner:
    def __init__(self, xp=0):
        self.xp=xp
        self.level = 1
        self.update_level()
    
    def mine(self, rock):
        current_rock = ROCKS[rock]
        level = current_rock[0]
        xp = current_rock[1]
        if (level <= self.level):
            self.xp+=xp
            levelled_up = self.update_level()
            if levelled_up: 
                return f"Congratulations, you just advanced a Mining level! Your mining level is now {self.level}."
            return 'You swing your pick at the rock.'
        else:
            return f'You need a mining level of {level} to mine {rock}.'
    def update_level(self):
        level = self.level
        xp = self.xp
        levels = list(EXPERIENCE.items())
        higher_levels = list(filter( lambda x: x[1] > xp, levels))
        if len(higher_levels) == 0:
            self.level = 40
            return False
        next_level = higher_levels[0][0]
        
        if next_level - 1 > self.level:
            self.level = next_level-1
            return True
        return False
        