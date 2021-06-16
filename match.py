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

        #  Prompt user to choose whether they want to
        #  duke it out with a bot, or if they want to go up
        #  against a buddy near by to see who wins.
        self.story()

        #  Display outro message. The winner will come
        #  from the outcome of the story the user steps
        #  into.
        self.display_outro(self.winner)

    #  endregion

    #  region Story
    def story(self):
        story_mode = input("\n\nDo you want to go up against "
                           "another person? Or do \nyou "
                           "want to go up against a bot?"
                           "\n\nEnter either 'Bots' or "
                           "'No Bots':\n\n")
        #  User choice is reached - two clear options:
        #  Option A: Human v. AI - bots
        #  Option B: Human v. Human - no bots
        self.game_mode(story_mode)
    #  endregion

    #  region Game_Mode
    def game_mode(self, the_choice):
        #  Option A: Human v. AI - self.player_two is a computer
        if the_choice.lower() == "bots":
            """
            player_one will always remain a Human(). 
            """
            self.player_one.player = input("\nEnter a nickname for yourself:\n\n")
            self.player_two = Computer("The God Bot")
            print(f"You're currently up against {self.player_two.player}\n\n")
            #  Ask the user if they're ready to play. They can change their settings here
            self.is_user_ready(the_choice)
            #  If the user is ready, the sequence of the game will begin in self.is_user_ready()
            #  After user enters into self.is_user_ready(), the game will need to finish before
            #  the final method in self.run_game() occurs (self.display_outro). The outro msg
            #  will display the winner of the game.
        #  Option B: Human v. Human - self.player_two is a human
        elif the_choice.lower() == "no bots":
            #  Instantiate players and give nicknames to them for clarity.
            self.player_one = Human("")
            self.player_two = Human("")
            self.player_one.player = input("\n\nPlayer one, enter a nickname:\n\n")
            self.player_two.player = input("\n\nPlayer two, enter a nickname:\n\n")
            #  Ask the user if they're ready to play. They can change their settings here
            self.is_user_ready(the_choice)
            #  If the user is ready, the sequence of the game will begin in self.is_user_ready()
            #  After user enters into self.is_user_ready(), the game will need to finish before
            #  the final method in self.run_game() occurs (self.display_outro). The outro msg
            #  will display the winner of the game.
        else:
            print("\n\nSorry, that's not an option. Please choose again.")
            #  If the user chooses anything other than "bots" or "no bots", they're re-prompted.
            self.story()

    #  endregion

    #  region Is_User_Ready
    def is_user_ready(self, human_or_bot):
        setting = input("Are you ready to play? Enter 'y' for yes, \n"
                        "or 'n' to change the settings for the game:\n\n")
        if setting.lower() == 'y':
            #  Based off of the bots or no bots choice given in self.game_mode()
            #  human_or_bot will dictate whether they go against a human or bot.
            self.bots_or_not(human_or_bot)
        elif setting.lower() == 'n':
            #  Prompt the user with settings to run specific story line
            self.story()
        else:
            #  If the user inputs anything other than 'y' or 'n', re-prompt
            print("That's not an option. Please try again.")
            self.is_user_ready(human_or_bot)
    #  endregion

    #  region Bots_Or_Not
    def bots_or_not(self, decision):
        #  The outcome of self.option_human_v_computer() will dictate the winner so
        #  that the self.display_outro will actually have a winner to display
        #  to the users. The same goes for self.option_human_v_human().
        if decision.lower() == "bots":
            self.option_human_v_computer()
        elif decision.lower() == "no bots":
            self.option_human_v_human()
    #  endregion

    #  region Option_Human_V_Computer
    def option_human_v_computer(self):
        gesture_results = Gesture()
        gesture_results.set_player_one(self.player_one)  # The person playing
        gesture_results.set_player_two(self.player_two)  # Should be human
        gesture_results.human_v_human()  # The game loop will occur here
        self.winner = gesture_results.get_the_winner()  # Game is finished, returns winner
        pass
    #  endregion

    #  region Option_Human_V_Human
    def option_human_v_human(self):
        #  The human will go up against another human
        gesture_results = Gesture()
        gesture_results.set_player_one(self.player_one)  # The person playing
        gesture_results.set_player_two(self.player_two)  # Should be human
        gesture_results.human_v_human()  # The game loop will occur here
        self.winner = gesture_results.get_the_winner()  # Game is finished, returns winner
    #  endregion

    #  region Display_Outro
    def display_outro(self):
        #  The winner comes from gesture_results.get_the_winner() in either one of the
        #  option methods above this one.
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
