from player import Player
import random
import time


class COPlayer(Player):

    def __init__(self, difficulty):
        super().__init__("🤖", 0)
        self.difficulty = difficulty

    def take_action(self, round_score):
        if self.difficulty == "easy" and round_score + self.total_score < 80:
            choice = random.choice(["r", "h"])
        elif self.difficulty == "hard" and round_score < 9:
            choice = "r"
        elif self.difficulty == "hard" and round_score >= 9:
            choice = random.choice(["r", "h"])
        elif self.difficulty == "hard" and round_score + self.total_score >= 90:
            choice = "r"
        elif self.difficulty == "hard" and round_score + self.total_score >= 100:
            choice = "h"
        # else:
        #     choice = "h"

        if choice == "r":
            time.sleep(1)
            print("Roll")
            time.sleep(1)
        else:
            time.sleep(1)
            print("Hold")
            time.sleep(1)
        return choice