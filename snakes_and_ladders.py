#snakes and ladders kata
#https://www.codewars.com/kata/587136ba2eefcb92a9000027

class SnakesLadders():

    def __init__(self):
        self.ladders_start = [2, 7, 8, 15, 21, 28, 36, 51, 71, 78, 87]
        self.ladders_end = [38, 14, 31, 26, 42, 84, 44, 67, 91, 98, 94]
        self.snakes_start = [16, 46, 49, 62, 64, 74, 89, 92, 95, 99]
        self.snakes_end = [6, 25, 11, 19, 60,  53, 68, 88, 75, 80]
        self.player_1 = 0
        self.player_2 = 0 
        self.complete = False
        self.player_turn = 1
        
    def snakes_ladders_check(self, position):
        if position in self.ladders_start:
            location = self.ladders_start.index(position)
            return self.ladders_end[location]
        elif position in self.snakes_start:
                location = self.snakes_start.index(position)
                return self.snakes_end[location]
        return position
        
    def isDouble(self, die1, die2):
        if not die1 == die2:
            if self.player_turn == 1:
                self.player_turn = 2

            else:
                self.player_turn = 1
            
            
    def play(self, die1, die2):
        if self.complete == True:
            return "Game over!"
        double = (die1 == die2)
        total = die1 + die2
        if self.player_turn == 1:
            
            self.player_1 += total
            print(self.player_1)
            if self.player_1 > 100:
                self.player_1 = 100 - abs(100-self.player_1)
            elif self.player_1 == 100: 
                self.complete = True
                return "Player 1 Wins!"
                
            self.player_1 = self.snakes_ladders_check(self.player_1)
            self.isDouble(die1, die2)
            return "Player 1 is on square {}".format(self.player_1)
            
        elif self.player_turn == 2:
            self.player_2 += total
            if self.player_2 > 100:
                self.player_2 = 100 - abs(100-self.player_2)
            elif self.player_2 == 100:
                self.complete = True
                return "Player 2 Wins!"
                
            self.player_2 = self.snakes_ladders_check(self.player_2)
            self.isDouble(die1, die2)
            return "Player 2 is on square {}".format(self.player_2)
