from gesture import Gesture


class Lizard(Gesture):
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
            #  Lizard is crushed by Rock
            #  self.player_one.loss()
            pass

        elif bravo_attack == "scissors":
            #  Lizard is decapitated by Scissors
            #  self.player_one.loss()
            pass

        elif bravo_attack == "paper":
            #  Lizard eats Paper
            #  self.player_two.loss()
            result = False

        elif bravo_attack == "spock":
            #  Lizard poisons Spock
            #  self.player_two.loss()
            result = False

        return result
    #  endregion
