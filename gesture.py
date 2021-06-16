class Gesture:
    def __init__(self, human, bot_or_human):
        self.match_winner = ""
        self.player_one = human
        self.player_two = bot_or_human
        self.human_v_human_result = False
        self.robot_v_robot_result = False
        self.loop = False

    def human_v_computer(self):
        the_final_result = ""
        the_final_result = "A human or computer can win"

        self.set_the_winner(the_final_result)

    def human_v_human(self):
        the_final_result = ""
        the_final_result = "Only a human can win"

        self.set_the_winner(the_final_result)

    def set_the_winner(self, the_winner):
        self.match_winner = the_winner

    def find_the_winner(self):
        return self.match_winner
