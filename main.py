"""
Just run this main, and the game will begin.
"""
from match import Match


#  This will create a new_match object that will allow
#  you to play Rock, Paper, Scissors, Lizard, Spock.
new_match = Match()

#  After creating the object, now the run_game() method
#  allows you to run the entire project in the console.
#  Disclaimer: The Human v Computer side is more fun
#  at the moment. Mostly because I haven't hid the
#  choices that the human players choose when it is
#  their turn.
new_match.run_game()
