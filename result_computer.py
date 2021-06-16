#  Loop to continue gameplay until best of 3, or;
#  One side has to get at least 2 wins out of 3 matches.
class ResultComputer:
    def __init__(self, human_one, comp_two):
        self.game_running = False
        self.champion = ""
        self.temp_one = human_one
        self.temp_two = comp_two

    def round(self):
        pass

    def game_over(self):
        pass

    def game_winner(self):
        return self.champion
