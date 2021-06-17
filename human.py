from player import Player


class Human(Player):
    #  region Constructor
    def __init__(self, the_name):
        super().__init__(the_name)  # Player also has lives
        self.the_gesture = ""
    #  endregion

    #  region Choose_Gesture overrides Choose_Gesture in Player()
    def choose_gesture(self):
        return self.gesture_options
    #  endregion

    #  region Special_Gesture overrides Special_Gesture in Player()
    def special_gesture(self, some_gesture):
        self.the_gesture = ""
        gesture_list = self.choose_gesture()
        for gesture in gesture_list:
            if some_gesture.lower() == gesture.lower():
                self.the_gesture = gesture.lower()
        return self.the_gesture
    #  endregion
