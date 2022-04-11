class SnakesLadders():

    def __init__(self):
        self.player_square = [] #list for position of players
        self.player_square.append(0)
        self.player_square.append(0)
        self.player = 0
        self.won = False
        self.trap = [[2,38],[7,14],[8,31],[15,26],[21,42],[28,84],[36,44],[51,67],[71,91],[78,98],[87,94],
                    [16,6],[46,25],[49,11],[62,19],[64,60],[74,53],[89,68],[92,88],[95,75],[99,80]] #list with position of laders and snakes

    def play(self, die1, die2):
        if self.won: 
            return "Game over!" #if someone allready won then return "Game over!" 
        b = die1 + die2 #sum of dies
        if b + self.player_square[self.player] <= 100:
            self.player_square[self.player] = self.player_square[self.player] + b #move player without bounce 
            if self.player_square[self.player] == 100: # check if player win
                self.won = True
                return "Player {who_won} Wins!".format(who_won=self.player+1)
        else:
            self.player_square[self.player] = 100 - ((self.player_square[self.player] + b) - 100) #move player with bounce
        for t in range(len(self.trap)):
            if self.player_square[self.player] == self.trap[t][0]:
                self.player_square[self.player] = self.trap[t][1] #move player on pos of lader or snake
            message = "Player "+str(self.player+1)+" is on square "+str(self.player_square[self.player]) 
        if die1 != die2: # return who will go next
            if self.player == 0:
                self.player = 1
            else:
                self.player = 0
        return message #return where is player