from gesture import Gesture


class Scissors(Gesture):
    #  region Constructor
    def __init__(self, human, bot_or_human):
        super().__init__(human, bot_or_human)
    #  endregion

    #  region Outcome
    def outcome(self, bravo_attack):
        #  If True, player_one.loss(), Else: player_two.loss()
        #  inside of Gesture(..., ...) class
        result = True

        if bravo_attack == "rock":
            #  Scissors are crushed by Rock
            #  self.player_one.loss()
            pass

        elif bravo_attack == "spock":
            #  Scissors are smashed by Spock
            #  self.player_one.loss()
            pass

        elif bravo_attack == "paper":
            #  Scissors cuts Paper
            #  self.player_two.loss()
            result = False

        elif bravo_attack == "lizard":
            #  Scissors decapitates Lizard
            #  self.player_two.loss()
            result = False

        return result
    #  endregion
