from computer import Computer
from gesture import Gesture
from human import Human


class Match:

    #  region Constructor
    def __init__(self):
        self.player_one = Human("Empty")
        self.player_two = None
        self.story_line = ""
        self.winner = ""
        self.game_running = False
    #  endregion

    #  region Run_Game
    def run_game(self):
        #  Display welcome screen

        self.display_welcome()

        #  Prompt user to choose whether they want to let
        #  the bots duke it out, or if they want to go up
        #  against a buddy near by to see who wins.

        self.story_line = input("\n\nDo you want to go up against "
                                "another person? Or do \nyou "
                                "want to let the bots go at it?"
                                "\n\nEnter either 'Bots' or "
                                "'No Bots':\n\n")

        #  User choice is reached - two clear options:
        #  Option A: Human v. AI
        #  Option B: Human v. Human

        self.game_mode(self.story_line)

        #  Display outro message

        self.display_outro(self.winner)

    #  endregion

    #  region Game_Mode
    def game_mode(self, the_choice):
        #  Option A: AI v. AI - self.player_two is human or computer
        if the_choice.lower() == "bots":
            """
            player_one will always remain a Human(). 
            """
            self.player_two = Computer("The God Bot")
            self.player_one.player = input("\nEnter a nickname?\n\n")
            print(f"Right now, you're up against {self.player_two.player}\n\n")
            self.game_running = True
            #  While game_running is true, keep playing
            while self.game_running:
                #  Enter sequence - return False when the game ends
                #  the_choice here will be "bots"
                self.game_running = self.player_options(the_choice)  # False when End Game
            #  The winner is declared inside player_one_options(..., ..., ...)
            self.winner = the_choice + "-- The Human v. AI storyline victor"
        #  Option B: Human v. Human
        elif the_choice.lower() == "no bots":
            """
            player_two will be where there be a condition allowing the 
            user to go up against either another human or the computer.
            """
            self.player_one = Human("")
            self.player_two = Human("")
            self.player_one.player = input("\n\nPlayer one, enter a nickname:\n\n")
            self.player_two.player = input("\n\nPlayer two, enter a nickname:\n\n")
            self.game_running = True
            #  While game_running is true, keep playing
            while self.game_running:
                #  Enter sequence - return False when the game ends
                #  the_choice here will be "no bots"
                self.game_running = self.player_options(the_choice)
            #  The winner is declared inside player_one_options(..., ..., ...)
            self.winner = the_choice + "-- The Human v. Human storyline victor"
        #  Option C: Invalid option. Try again.
        else:
            print("\n\nSorry, that's not an option. Please choose again.")
            a_choice = input("\n'Bots' or 'No Bots:\n\n")
            #  Re-enter game_mode(...) decision-making process
            self.game_mode(a_choice)
    #  endregion

    def player_options(self, decision):
        the_result = True

        while the_result:
            if decision.lower() == "bots":
                #  They will hash it out.
                the_result = False  # Change once gameplay for human_v_human is finished
                #  Will come back to this portion.

            elif decision.lower() == "no bots":
                #  The human will go up against another human
                gesture_results = Gesture()
                gesture_results.set_player_two(self.player_two)  # Should be human
                the_result = gesture_results.human_v_human()  # False when End Game
            else:
                #  Ever...
                print("This should not print")
            return the_result
        pass

    #  region Display_Outro
    def display_outro(self, the_winner):
        self.winner = the_winner
        print(f"\n\nAnd the winner for this game is: {self.winner}")
    #  endregion

    #  region Display_Welcome
    def display_welcome(self):
        print("\n\nWelcome to Rock, Paper, Scissors, Lizard, Spock\n\n")

        #  Indicate rules of the match
        print("Here are some rules are before you get started:\n\n"
              "First: Pick whether you want to go against another\n"
              "human, or if you want the computer to go against a\n"
              "bot.\n\n"
              "Second: You are only allowed three lives per game.\n"
              "So, if you decide to let the computer play in your\n"
              "place, the computer and the opponent will only have\n"
              "three total lives.\n\n"
              "Third: Finally, the winner will be decided once the\n"
              "loser has no lives left in the game.\n\n"
              "And that's it!")
    #  endregion