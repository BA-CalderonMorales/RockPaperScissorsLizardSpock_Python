from player import Player


class Human(Player):
    def __init__(self, human_name):
        super().__init__()  # Player also has lives
        self.name = human_name