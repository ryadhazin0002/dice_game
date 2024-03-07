from player import Player
import time


class Display:

    def __init__(self, delay) -> None:
        self.delay = delay
        pass

    def display_draw(self):
        try:
            print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
            print(f"🎉🎉🎉 DRAW !!!! 🎉🎉🎉")
            print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
        except:
            print("DRAW!!!")

    def display_congratulations(self, winner: Player):
        try:
            print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
            print(f"🎉🎉🎉 congratulations {winner.name} won 🎉🎉🎉")
            print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
        except:
            print(f"congratulations {winner.name} won")

    def display_dice_value_and_round_score(self, diceValue, round_score):
        print(f"dice {diceValue}")
        print(f"Your current score is {round_score}")
        print("Press 'Q' to exit")
        print("Press 'R' to restart")

    def display_main_menu(self):
        """Display main menu"""
        print()
        print("*******************************")
        try:
            print("🎲 Welcome to Pig Dice Game 🎲")
        except:
            print(" Welcome to Pig Dice Game ")
        print("*******************************")
        print()
        print("1. Start new game")
        print("2. Player's Highscore")
        print("3. Rules of the game")
        print("4. Change player's name")
        print("5. Exit")
        return input("Your choice: ")

    def display_new_game_menu(self):
        """Display new game Menu"""
        print("1. CO-Player")
        print("2. Multi-Player")
        return input("Your choice: ")

    def display_co_player_level(self):
        """Display CoPlayer level"""
        print("1. Easy")
        print("2. Hard")
        return input("Your choice: ")

    def display_game_rules(self):
        """Display game rules"""
        try:
            print("🎲 Pig Dice Game Rules🎲")
            print()
            print(
                "🧩 Objective:🧩\nBe the first player to"
                " reach a total score of 100 points."
            )
            print("Equipment: 1 standard six-sided dice")
            print()
            time.sleep(1 * self.delay)
            print("🕹️  Gameplay:🕹️")
            print("1. Players take turns rolling the dice during their turn.")
            print("2. Players take turns rolling the dice during their turn.")
            print(
                "3. If a player rolls a 2-6, they add that number to their "
                "turn total and can choose to either roll again or "
                "end their turn."
            )
            print(
                "4. If a player chooses to end their turn, they add the turn"
                " total to their overall score."
            )
            print(
                "5. Rolling a 1 during subsequent rolls forfeits all points"
                " gained in that turn."
            )
            print()
            time.sleep(1 * self.delay)
            print("🎊 Winning:🎊")
            print("The first player to reach or exceed 100 points wins the game.🥇")
            print()
            time.sleep(1 * self.delay)
            print("🤓 Strategy:🤓")
            print(
                "Decide wisely when to stop rolling and 'bank' the points to "
                "avoid losing them on a subsequent roll."
            )
            print()
            time.sleep(1 * self.delay)
            print("🎲 Enjoy the game!🎲")
        except:
            print()
