from human import Human
from result_human import ResultHuman


class Gesture:
    def __init__(self):
        self.player_one = Human("")
        self.player_two = None
        self.match_winner = ""
        self.human_v_human_result = False
        self.robot_v_robot_result = False

    def human_v_human(self):
        result: bool = False
        match_result = ResultHuman()  # The human v. human match begins and ends here
        result = match_result.game_over()  # The result of the match is here
        self.match_winner = match_result.game_winner()  # The winner is here

    def set_player_two(self, player):
        self.player_one = player

    def set_player_two(self, comp_or_human):
        self.player_two = comp_or_human

    def get_the_winner(self):
        return self.match_winner  # Returns the winner of the match
