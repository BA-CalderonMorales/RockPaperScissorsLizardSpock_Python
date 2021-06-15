from random import random
from player import Player


class Computer(Player):

    #  region Constructor
    def __init__(self, comp_name):
        super().__init__(comp_name)  # Player also has lives
    #  endregion

    #  region Choose_Gesture overrides Player() Choose_Gesture
    def choose_gesture(self):
        rand = random.randint(0, 4)
        self.the_gesture = self.gesture_options[rand]
    #  endregion