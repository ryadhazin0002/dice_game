from player import Player
import random
import time


class COPlayer(Player):

    def __init__(self):
        super().__init__("🤖", 0)

    def take_action(self):
        choice = random.choice(["r", "h"])
        if choice == "r":
            time.sleep(1)
            print("Roll")
            time.sleep(1)
        else:
            time.sleep(1)
            print("Hold")
            time.sleep(1)
        return choice 