#  Loop to continue gameplay until best of 3, or;
#  One side has to get at least 2 wins out of 3 matches.
from gesture import Gesture


class ResultComputer(Gesture):
    def __init__(self):
        super().__init__()
        self.champion = ""

    def game_over(self):
        pass

    def game_winner(self):
        return self.champion