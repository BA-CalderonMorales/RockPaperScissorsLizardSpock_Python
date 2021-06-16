from human import Human
from player import Player
from result_human import ResultHuman


class Gesture:
    def __init__(self, human, bot_or_human):
        self.match_winner = Player("Empty")
        self.player_one = human
        self.player_two = bot_or_human
        self.human_v_human_result = False
        self.robot_v_robot_result = False
        self.loop = True

    def human_v_computer(self):
        while self.loop:
            a_round = ResultHuman(self.player_one, self.player_two)
            a_round.update_loop(self.loop)
            if a_round.loop_result():
                print("This is the start of the human v computer loop")

                #  Keep the rounds going
                #  Stop if a certain condition is met
                self.loop = False
                a_round.update_loop(self.loop)
            else:
                #  Because we don't know whether it will be a Human or a Computer
                self.set_the_winner(Player("Some winner - Human or Computer"))

    def human_v_human(self):
        while self.loop:
            a_round = ResultHuman(self.player_one, self.player_two)
            a_round.update_loop(self.loop)
            if a_round.loop_result():
                print("This is the start of the human v human loop")

                #  Keep the rounds going
                #  Stop if a certain condition is met
                self.loop = False
                a_round.update_loop(self.loop)
            else:
                #  Because we know the outcome can only be a Human
                self.set_the_winner(Human("Some winner - Can only be Human"))

    def set_the_winner(self, the_winner):
        self.match_winner = the_winner

    def find_the_winner(self):
        return self.match_winner
