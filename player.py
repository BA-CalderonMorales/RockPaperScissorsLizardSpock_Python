class Player:
    #  region Thoughts before starting project
    """
    As a player, the game should have an option of having a
    human go up against an AI, or a human going up against
    another human.
    """
    #  endregion

    #  region Constructor
    def __init__(self, the_name):
        self.player = the_name  # Can be an AI or human
        self.gesture_options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.the_gesture = ""
        self.score = 0  # Dictates player lives
    #  endregion

    #  region Gestures
    def gestures(self):
        for index in range(0, len(self.gesture_options)):
            print(f"{self.gesture_options[index]}\n")
    #  endregion

    #  region Choose_Gesture
    def choose_gesture(self):
        print("Override this method")
        pass
    #  endregion