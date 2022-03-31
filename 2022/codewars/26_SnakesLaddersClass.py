def snake(player):
    if player == 99:
        player = 80
    elif player == 95:
        player = 75
    elif player == 92:
        player = 88
    elif player == 89:
        player = 68
    elif player == 74:
        player = 53
    elif player == 64:
        player = 60
    elif player == 62:
        player = 19
    elif player == 49:
        player = 11
    elif player == 46:
        player = 25
    elif player == 16:
        player = 6
    return player


def ladder(player):
    player = snake(player)
    if player == 2:
        player = 38
    elif player == 7:
        player = 14
    elif player == 8:
        player = 31
    elif player == 15:
        player = 26
    elif player == 21:
        player = 42
    elif player == 28:
        player = 84
    elif player == 36:
        player = 44
    elif player == 51:
        player = 67
    elif player == 71:
        player = 91
    elif player == 78:
        player = 98
    elif player == 87:
        player = 94
    return player


class SnakesLadders():

    def __init__(self):
        self.player1 = 0
        self.player2 = 0
        self.queue = 0

    def play(self, die1, die2):
        if self.player1 == 100 or self.player2 == 100:
            return 'Game over!'
        if self.queue % 2 == 0:
            self.player1 += die1 + die2
            if self.player1 == 100:
                return 'Player 1 Wins!'
            if self.player1 > 100:
                self.player1 -= 100
                self.player1 = 100 - self.player1
            self.player1 = ladder(self.player1)
            if die1 != die2:
                self.queue += 1
            return f'Player 1 is on square {self.player1}'
        else:
            self.player2 += die1 + die2
            if self.player2 == 100:
                return 'Player 2 Wins!'
            if self.player2 > 100:
                self.player2 -= 100
                self.player2 = 100 - self.player2
            self.player2 = ladder(self.player2)
            if die1 != die2:
                self.queue += 1
            return f'Player 2 is on square {self.player2}'
