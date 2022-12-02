
from enum import Enum

class Hand(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
class Outcome(Enum):
    WIN = 6
    LOSE = 0
    DRAW = 3
    
class Game():
    def __init__(self, i_string):
        self.o= i_string.split(' ')[0]
        self.m = i_string.split(' ')[1]
        
        #Determine other player hand
        if self.o == 'A': #Rock
            self.o_hand = Hand.ROCK
        elif self.o == 'B': #Paper
            self.o_hand = Hand.PAPER
        elif self.o == 'C': #Scissors
            self.o_hand = Hand.SCISSORS
        
        #Determine my hand
        if self.m == 'X': #Rock
            self.p1_hand = Hand.ROCK
            self.p2_outcome = Outcome.LOSE
        elif self.m == 'Y': #Paper
            self.p1_hand = Hand.PAPER
            self.p2_outcome = Outcome.DRAW
        elif self.m == 'Z': #Scissors
            self.p1_hand = Hand.SCISSORS
            self.p2_outcome = Outcome.WIN
    
    def p1_result(self):
        if self.o_hand == self.p1_hand:
            return self.p1_hand.value + Outcome.DRAW.value
        elif self.p1_hand == Hand.ROCK and self.o_hand == Hand.SCISSORS:
            return self.p1_hand.value + Outcome.WIN.value
        elif self.p1_hand == Hand.PAPER and self.o_hand == Hand.ROCK:
            return self.p1_hand.value  + Outcome.WIN.value
        elif self.p1_hand == Hand.SCISSORS and self.o_hand == Hand.PAPER:
            return self.p1_hand.value  + Outcome.WIN.value
        else:
            return self.p1_hand.value  + Outcome.LOSE.value
        
    def p2_result(self):
        if self.p2_outcome == Outcome.DRAW:
            self.p2_hand = self.o_hand
        elif self.p2_outcome == Outcome.WIN:
            if self.o_hand == Hand.ROCK:
                self.p2_hand = Hand.PAPER
            elif self.o_hand == Hand.PAPER:
                self.p2_hand = Hand.SCISSORS
            elif self.o_hand == Hand.SCISSORS:
                self.p2_hand = Hand.ROCK
        else:   #Lose
            if self.o_hand == Hand.ROCK:
                self.p2_hand = Hand.SCISSORS
            elif self.o_hand == Hand.PAPER:
                self.p2_hand = Hand.ROCK
            elif self.o_hand == Hand.SCISSORS:
                self.p2_hand = Hand.PAPER
        return self.p2_hand.value + self.p2_outcome.value

def parse_input(ifile = "input.txt"):
    games = []
    with open(ifile) as ifile:
        for line in ifile.readlines():
            games.append(Game(line.strip()))
    return games

def p1_solve(games:list):
    total_score = 0
    for game in games:
        total_score += game.p1_result()
    return total_score

def p2_solve(games:list):
    total_score = 0
    for game in games:
        total_score += game.p2_result()
    return total_score

if __name__ == '__main__':
    games = parse_input()
    #games = parse_input('sampleinput.txt')
    print('Part 1 Solution: {0}'.format(p1_solve(games)))
    print('Part 2 Solution: {0}'.format(p2_solve(games)))

