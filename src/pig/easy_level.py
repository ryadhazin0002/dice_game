from intelligence import Intelligence
import random
import time


class Easy(Intelligence):

    def __init__(self, delay) -> None:
        """Init for Easy class"""
        self.delay = delay
        super().__init__()

    def playing_logic(self, total_score: int, current_score: int):
        """Playing logic for choice (randomly between Roll and Hold)"""
        round_score = self.calc_round_score(total_score, current_score)
        choice = random.choice(["r", "h"])
        if choice == "r":
            time.sleep(1 * self.delay)
            print("Roll")
            time.sleep(1 * self.delay)
        else:
            time.sleep(1 * self.delay)
            print("Hold")
            time.sleep(1 * self.delay)
        return choice
