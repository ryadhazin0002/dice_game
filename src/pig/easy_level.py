from intelligence import Intelligence
import random
import time


class Easy(Intelligence):

    def __init__(self) -> None:
        super().__init__()

    def playing_logic(self, total_score: int, current_score: int):
        round_score = self.calc_round_score(total_score, current_score)
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
