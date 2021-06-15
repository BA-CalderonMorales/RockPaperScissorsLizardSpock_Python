from rich.console import Console
from time import sleep

class Match():
    def __init__(self):
        self.alpha = ""
        self.bravo = ""

    def run_game(self):
        #  Display welcome screen

        #  Indicate rules of the match

        #  Prompt user to choose whether
        #  They want to go against the
        #  bot, or if the bots should go
        #  against each other.

        #  User choice is reached, two
        #  clear options:

        #  Option A: Human v. AI
        #  Winner is decided, display winner

        #  Option B: Human v. Human
        #  Winner is decided, display winner

        #  Display outro message
        pass

    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock")
        console = Console()
        tasks = [f"task {n}" for n in range(1, 11)]

        with console.status("[bold green] Waiting on user input...") as status:
            while tasks:
                task = tasks.pop(0)
                sleep(1)
                console.log(f"{task} complete")
