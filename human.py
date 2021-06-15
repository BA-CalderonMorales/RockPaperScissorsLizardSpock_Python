from player import Player


class Human(Player):
    #  region Constructor
    def __init__(self, the_name):
        super().__init__(the_name)  # Player also has lives
        self.the_gesture = ""
    #  endregion

    #  region Choose_Gesture overrides Choose_Gesture in Player()
    def choose_gesture(self):
        self.the_gesture = self.get_gesture()
    #  endregion

    #  region Set_Gesture
    def set_gesture(self, human_input):
        self.the_gesture = human_input
    #  endregion

    #  region Get_Gesture
    def get_gesture(self):
        return self.the_gesture
    #  endregion