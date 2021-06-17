from player import Player
import random


class Computer(Player):

    #  region Constructor
    def __init__(self, comp_name):
        super().__init__(comp_name)  # Player also has lives

    #  endregion

    #  region Choose_Gesture overrides Player() Choose_Gesture
    def choose_gesture(self):
        #  This method is overriding the choose_gestures method in
        #  the Player class.
        rand = random.randint(0, 4)
        self.the_gesture = self.gesture_options[rand].lower()
    #  endregion

    #  region Get_Gesture overrides Player Get_Gesture
    def get_gesture(self):
        self.choose_gesture()
        return self.the_gesture

