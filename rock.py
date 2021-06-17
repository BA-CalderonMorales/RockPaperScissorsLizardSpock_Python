from gesture import Gesture


class Rock(Gesture):
    def __init__(self, human, bot_or_human):
        super().__init__(human, bot_or_human)

    def outcome(self, bravo_attack):
        #  If True, player_one.loss(), Else: player_two.loss()
        #  inside of Gesture(..., ...) class
        result = True

        if bravo_attack == "paper":
            #  Rock is covered by paper
            #  self.player_two.loss()
            result = False

        elif bravo_attack == "spock":
            #  Rock is vaporized by Spock
            #  self.player_two.loss()
            result = False

        elif bravo_attack == "scissors":
            #  Rock crushes Scissors
            #  self.player_one.loss()
            pass  # result = True

        elif bravo_attack == "lizard":
            #  Rock crushes Lizard
            #  self.player_one.loss()
            pass  # result = True

        return result