from player import Player


class Computer(Player):
    def __init__(self, comp_name):
        super().__init__()  # Player also has lives
        self.name = comp_name
