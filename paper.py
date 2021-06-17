from gesture import Gesture


class Paper(Gesture):
    def __init__(self, human, bot_or_human):
        super().__init__(human, bot_or_human)

    def outcome(self, bravo_attack):
        #  If True, player_one.loss(), Else: player_two.loss()
        #  inside of Gesture(..., ...) class
        result = True

        if bravo_attack == "scissors":
            #  Paper is cut by Scissors
            #  self.player_two.loss()
            result = False

        elif bravo_attack == "lizard":
            #  Paper is eaten by Lizard
            #  self.player_two.loss()
            result = False

        elif bravo_attack == "rock":
            #  Paper covers Rock
            #  self.player_one.loss()
            pass  # result = True

        elif bravo_attack == "spock":
            #  Paper disproves Spock
            #  self.player_one.loss()
            pass  # result = True

        return result
