from player import Player
from human import Human


class Gesture:
    #  region Constructor
    def __init__(self, human, bot_or_human):
        self.match_winner = Player("Empty")
        self.player_one = Human(human)
        self.player_two = Player(bot_or_human)
        self.loop = True
    #  endregion

    #  region Human_v_Computer
    def human_v_computer(self):
        current_game_state = self.loop
        count = 1
        print(f"\nThis is the start of round {count}\n")
        while current_game_state:
            if current_game_state:
                #  User input is taken in from player_one only.
                self.player_one.gestures()
                one_input = input(f"{self.player_one.player}, pick a gesture from above by typing "
                                  "the gesture name:\n\n")

                #  Each user is assigned a gesture for this round. A gesture is returned (i.e. rock, paper, ...)
                player_one_gesture = self.player_one.special_gesture(one_input)
                #  Player two is a bot, so their chosen gesture will be random.
                player_two_gesture = self.player_two.get_gesture()
                print(f"\nLooks like {self.player_two.player} chose: {self.player_two.the_gesture}")

                #  Get a result from the current round, based off of game rules and previous method.
                self.get_round_result(player_one_gesture, player_two_gesture)

                """
                This portion of code was commented out so that you can check the 
                amount of turns/lives that the player currently would have after
                each round.

                print(f"{self.player_one.player} currently has "
                      f"{self.player_one.lives} lives left")
                print(f"{self.player_two.player} currently has "
                      f"{self.player_two.lives} lives left")
                """

                #  If self.get_round_result takes too many lives away from one or the other person, then
                #  the game will end in the following bit of code.
                self.loop = self.end_game_logic_computer()
                if not self.loop:
                    #  Stop if a certain condition is met
                    current_game_state = self.loop
                    self.update_loop(self.loop)
                else:
                    count += 1
                    print(f"\nRound: {count}\n")
    #  endregion

    #  region Human_v_Human
    def human_v_human(self):
        current_game_state = self.loop
        count = 1
        print(f"\nThis is the start of round {count}\n")
        while current_game_state:
            if current_game_state:
                #  User input is taken in from both humans.
                self.player_one.gestures()
                one_input = input(f"{self.player_one.player}, pick a gesture from above by typing "
                                  "the gesture name:\n\n")
                two_input = input(f"\n{self.player_two.player}, pick a gesture from above by typing "
                                  f"the gesture name:\n\n")

                #  Each user is assigned a gesture for this round. A gesture is returned (i.e. rock, paper, ...)
                player_one_gesture = self.player_one.special_gesture(one_input)
                player_two_gesture = self.player_two.special_gesture(two_input)

                #  Get a result from the current round, based off of game rules and previous method.
                self.get_round_result(player_one_gesture, player_two_gesture)

                """
                This portion of code was commented out so that you can check the 
                amount of turns/lives that the player currently would have after
                each round.
                
                print(f"{self.player_one.player} currently has "
                      f"{self.player_one.lives} lives left")
                print(f"{self.player_two.player} currently has "
                      f"{self.player_two.lives} lives left")
                """

                #  If self.get_round_result takes too many lives away from one or the other person, then
                #  the game will end in the following bit of code.
                self.loop = self.end_game_logic_human()
                if not self.loop:
                    #  Stop if a certain condition is met
                    current_game_state = self.loop
                    self.update_loop(self.loop)
                else:
                    count += 1
                    print(f"\n\nRound: {count}\n")
    #  endregion

    #  region Set_Player_One
    def set_player_one(self, one):
        self.player_one = one
    #  endregion

    #  region Set_Player_Two
    def set_player_two(self, two):
        self.player_two = two
    #  endregion

    #  region Set_The_Winnder
    def set_the_winner(self, the_winner):
        self.match_winner = the_winner
    #  endregion

    #  region Find_The_Winner
    def find_the_winner(self):
        return self.match_winner
    #  endregion

    #  region Get_Round_Result
    def get_round_result(self, one, two):
        from rock import Rock
        rock_choice = Rock(self.player_one, self.player_two)
        from paper import Paper
        paper_choice = Paper(self.player_one, self.player_two)
        from scissors import Scissors
        scissors_choice = Scissors(self.player_one, self.player_two)
        from lizard import Lizard
        lizard_choice = Lizard(self.player_one, self.player_two)
        from spock import Spock
        spock_choice = Spock(self.player_one, self.player_two)

        # Dictates who takes a loss
        player_one_or_player_two = False

        # Dictates a tie
        a_tie = ""

        #  Nothing happens to the lives of either player
        if one == "rock" and two == "rock" \
                or one == "paper" and two == "paper" \
                or one == "scissors" and two == "scissors" \
                or one == "lizard" and two == "lizard" \
                or one == "spock" and two == "spock":
            a_tie = "tie"

        #  One player will have less lives - Rock
        elif one == "rock" and two == "paper" \
                or one == "rock" and two == "scissors" \
                or one == "rock" and two == "lizard" \
                or one == "rock" and two == "spock":
            player_one_or_player_two = rock_choice.outcome(two)

        #  One player will have less lives - Paper
        elif one == "paper" and two == "rock" \
                or one == "paper" and two == "scissors" \
                or one == "paper" and two == "lizard" \
                or one == "paper" and two == "spock":
            player_one_or_player_two = paper_choice.outcome(two)

        #  One player will have less lives - Scissors
        elif one == "scissors" and two == "rock" \
                or one == "scissors" and two == "paper" \
                or one == "scissors" and two == "lizard" \
                or one == "scissors" and two == "spock":
            player_one_or_player_two = scissors_choice.outcome(two)

        #  One player will have less lives - Lizard
        elif one == "lizard" and two == "rock" \
                or one == "lizard" and two == "paper" \
                or one == "lizard" and two == "scissors" \
                or one == "lizard" and two == "spock":
            player_one_or_player_two = lizard_choice.outcome(two)

        #  One player will have less lives - Spock
        elif one == "spock" and two == "paper" \
                or one == "spock" and two == "scissors" \
                or one == "spock" and two == "lizard" \
                or one == "spock" and two == "spock":
            player_one_or_player_two = spock_choice.outcome(two)
        #  Based off the true or false value from the match,
        #  If True, player_one.loss(), Else: player_two.loss()
        self.set_round_result(player_one_or_player_two, a_tie)
    #  endregion

    #  region Set_Round_Result
    def set_round_result(self, round_outcome, tie):
        if tie == "tie":
            pass
        elif round_outcome:
            self.player_one.loss()
        else:
            self.player_two.loss()
    #  endregion

    #  region End_Game_Logic_Computer
    def end_game_logic_computer(self):
        result = True
        if self.player_one.lives >= 1 and self.player_two.lives <= 0:
            self.set_the_winner(self.player_one)
            result = False
        elif self.player_one.lives == 2 and self.player_two.lives == 0:
            self.set_the_winner(self.player_one)
            result = False
        elif self.player_one.lives <= 0 and self.player_two.lives >= 1:
            self.set_the_winner(self.player_two)
            result = False
        elif self.player_one.lives == 0 and self.player_two.lives == 2:
            self.set_the_winner(self.player_two)
            result = False

        return result
    #  endregion

    #  region End_Game_Logic_Human
    def end_game_logic_human(self):
        result = True
        if self.player_one.lives >= 1 and self.player_two.lives <= 0:
            self.set_the_winner(self.player_one)
            result = False
        elif self.player_one.lives == 2 and self.player_two.lives == 0:
            self.set_the_winner(self.player_one)
            result = False
        elif self.player_one.lives <= 0 and self.player_two.lives >= 1:
            self.set_the_winner(self.player_two)
            result = False
        elif self.player_one.lives == 0 and self.player_two.lives == 2:
            self.set_the_winner(self.player_two)
            result = False

        return result
    #  endregion

    #  region Get_Loop_State
    def get_loop_state(self):
        return self.loop
    #  endregion

    #  region Update_Loop
    def update_loop(self, true_or_false):
        self.loop = true_or_false
    #  endregion