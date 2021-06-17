from computer import Computer
from player import Player
from human import Human
from gesture import Gesture


class Match:

    #  region Constructor
    def __init__(self):
        self.player_one = Human("Empty")
        self.player_two = Player("Empty")
        self.gesture_results = Gesture(None, None)
        self.story_line = ""
        self.winner = Player("Empty")

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
        #  into. self.gesture_results temporarily holds the
        #  results from the end of a match and then sets
        #  it equal to self.winner.
        self.display_outro()

    #  endregion

    #  region Story
    def story(self):
        story_mode = input("\nSo, do you want to go up against "
                           "another person? Or do "
                           "\nyou want to go up against a bot?"
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
        if the_choice.lower().strip() == "bots":
            """
            player_one will always remain a Human(). 
            """
            self.player_one.player = input("\nEnter a nickname for yourself:\n\n")
            self.player_two = Computer("The God Bot")
            print(f"\nYou're currently up against {self.player_two.player}")
            #  Ask the user if they're ready to play. They can change their settings here
            self.is_user_ready(the_choice)
            #  If the user is ready, the sequence of the game will begin in self.is_user_ready()
            #  After user enters into self.is_user_ready(), the game will need to finish before
            #  the final method in self.run_game() occurs (self.display_outro). The outro msg
            #  will display the winner of the game.
        #  Option B: Human v. Human - self.player_two is a human
        elif the_choice.lower().strip() == "no bots":
            #  Instantiate players and give nicknames to them for clarity.
            self.player_one = Human("")
            self.player_two = Human("")
            self.player_one.player = input("\nPlayer one, enter a nickname:\n\n")
            self.player_two.player = input("\nPlayer two, enter a nickname:\n\n")
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
        setting = input("\nAre you ready to play? Enter 'y' for yes, \n"
                        "or 'n' to change the settings for the game:\n\n")
        if setting.lower().strip() == 'y':
            #  Based off of the bots or no bots choice given in self.game_mode()
            #  human_or_bot will dictate whether they go against a human or bot.
            self.bots_or_not(human_or_bot)
        elif setting.lower().strip() == 'n':
            #  Prompt the user with settings to run specific story line
            self.story()
        else:
            #  If the user inputs anything other than 'y' or 'n', re-prompt
            print("\nThat's not an option. Please try again.\n")
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
        #  The human will go up against the computer
        #  Instantiate a Gesture object.
        #  print(f"{self.player_one.player}"), verified that it was player_one
        #  print(f"{self.player_two.player}"), verified that it was player_two
        self.gesture_results.set_player_one(self.player_one)
        self.gesture_results.set_player_two(self.player_two)

        #  The gesture_results.human_v_computer should set the value of self.winner inside
        #  of the Gesture class.
        self.gesture_results.human_v_computer()  # The game loop will occur here, no return value

        #  Then, the value inside of the Gesture class (self.match_winner), will be called
        #  by following the logic below.  The winner is now set and can be displayed in
        #  self.display_outro(self).
        self.winner = self.gesture_results.find_the_winner()

    #  endregion

    #  region Option_Human_V_Human
    def option_human_v_human(self):
        #  The human will go up against another human
        #  Instantiate a Gesture object.
        #  print(f"{self.player_one.player}"), verified that it was player_one
        #  print(f"{self.player_two.player}"), verified that it was player_two
        self.gesture_results.set_player_one(self.player_one)
        self.gesture_results.set_player_two(self.player_two)

        #  The gesture_results.human_v_human should set the value of self.winner inside
        #  of the Gesture class.
        self.gesture_results.human_v_human()  # The game loop will occur here, no return value

        #  Then, the value inside of the Gesture class (self.match_winner), will be called
        #  by following the logic below.  The winner is now set and can be displayed in
        #  self.display_outro(self).
        self.winner = self.gesture_results.find_the_winner()

    #  endregion

    #  region Display_Outro
    def display_outro(self):
        self.winner = self.gesture_results.find_the_winner()
        #  The winner comes from gesture_results.get_the_winner() in either one of the
        #  option methods above this one.
        print(f"\n\nAnd the winner for this match is: {self.winner.player}\n")
        choice = input("Do you want to play again? Enter 'y' for yes "
                       "or 'n' for no: \n\n")
        self.replay_game(choice)
    #  endregion

    #  region Display_Welcome
    def display_welcome(self):
        print("\n\nWelcome to Rock, Paper, Scissors, Lizard, Spock\n\n")

        #  Indicate rules of the match
        print("Here are some rules before you get started:\n\n"
              "1) Pick whether you want to go against another\n"
              "human, or if you want to go against a bot.\n\n"
              "2) It follows that a player must win 2 out "
              "of 3\n"
              "rounds two win the match.\n\n"
              "3) Finally, if there is a tie, the game will keep\n"
              "going until one player wins 2 out of 3 total "
              "rounds.\n\n"
              "And that's it!")

    #  endregion

    #  region Replay_Game
    def replay_game(self, option):
        if option.lower().strip() == 'y':
            self.story()
        elif option.lower().strip() == 'n':
            print("\nTake care!")
        else:
            print("\nThat's not an option. Please try again.\n")
            choice = input("Do you want to play again? Enter 'y' for yes "
                           "or 'n' for no: \n")
            self.replay_game(choice)
    #  endregion
