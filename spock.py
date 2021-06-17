from gesture import Gesture


class Spock(Gesture):
    def __init__(self, human, bot_or_human):
        super().__init__(human, bot_or_human)

    def outcome(self, bravo_attack):
        #  If True, player_one.loss(), Else: player_two.loss()
        #  inside of Gesture(..., ...) class
        result = True

        if bravo_attack == "paper":
            #  Spock is disproved by Paper
            #  self.player_two.loss()
            result = False

        elif bravo_attack == "lizard":
            #  Spock is poisoned by Lizard
            #  self.player_two.loss()
            result = False

        elif bravo_attack == "rock":
            #  Spock vaporizes Rock
            #  self.player_one.loss()
            pass  # result = True

        elif bravo_attack == "scissors":
            #  Spock smashes Scissors
            #  self.player_one.loss()
            pass  # result = True

        return result