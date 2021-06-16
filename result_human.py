#  Loop to continue gameplay until best of 3, or;
#  One side has to get at least 2 wins out of 3 matches.
from gesture import Gesture


class ResultHuman(Gesture):
    def __init__(self):
        super().__init__()
        self.champion = ""

    def game_over(self):
        game_running = True
        while game_running:
            print("\n\nChoose a gesture: ")


    def game_winner(self):
        return self.champion