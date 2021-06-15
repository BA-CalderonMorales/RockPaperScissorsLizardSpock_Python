from human import Human


class Gesture:
    def __init__(self):
        self.player_one = Human("")
        self.player_two = None

    def human_v_human(self):
        result: bool = False

        #  Loop to continue gameplay until best of 3, or;
        #  One side has to get at least 2 wins out of 3 matches.

        print("\n\nHere are the list of gestures to choose from\n\n")
        self.player_one.gestures()
        data_alpha = input("Go ahead and enter a gesture from the list above: ")

        self.player_one.choose_gesture(data_alpha)
        print("Now tell your opponent to come over and let them input a gesture.")
        data_bravo = input("Enter gesture here: ")
        self.player_two.choose_gesture(data_bravo)

        if data_alpha == "Rock" and data_bravo == "Rock" \
                or data_alpha == "Paper" and data_bravo == "Paper" \
                or data_alpha == "Scissors" and data_bravo == "Scissors":
            print("Draw! Go again.")
            self.human_v_human()

        return result

    def set_player_two(self, comp_or_human):
        self.player_two = comp_or_human
