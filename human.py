from player import Player


class Human(Player):
    #  region Constructor
    def __init__(self, the_name):
        super().__init__(the_name)  # Player also has lives
        self.the_gesture = ""
    #  endregion

    #  region Choose_Gesture overrides Choose_Gesture in Player()
    def choose_gesture(self, some_gesture):
        current_gesture = some_gesture
        if current_gesture.lower() == "rock":
            chosen_gesture = some_gesture
        elif current_gesture.lower() == "paper":
            chosen_gesture = some_gesture
        elif current_gesture.lower() == "scissors":
            chosen_gesture = some_gesture
        elif current_gesture.lower() == "lizard":
            chosen_gesture = some_gesture
        elif current_gesture.lower() == "spock":
            chosen_gesture = some_gesture
        else:
            print("That's not a gesture, you get rock "
                  "for picking a nonexistent gesture.")
            chosen_gesture = "rock"
        #  Allows for user to pick any gesture in the option list.
        return chosen_gesture
    #  endregion