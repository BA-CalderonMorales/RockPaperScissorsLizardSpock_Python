from gesture import Gesture


class Paper(Gesture):
    #  region Constructor
    def __init__(self, human, bot_or_human):
        super().__init__(human, bot_or_human)
    #  endregion

    #  region Outcome
    def outcome(self, bravo_attack):
        #  If True, player_one.loss(), Else: player_two.loss()
        #  inside of Gesture(..., ...) class
        result = True

        if bravo_attack == "scissors":
            #  Paper is cut by Scissors
            #  self.player_one.loss()
            pass

        elif bravo_attack == "lizard":
            #  Paper is eaten by Lizard
            #  self.player_one.loss()
            pass

        elif bravo_attack == "rock":
            #  Paper covers Rock
            #  self.player_two.loss()
            result = False

        elif bravo_attack == "spock":
            #  Paper disproves Spock
            #  self.player_two.loss()
            result = False

        return result
    #  endregion
