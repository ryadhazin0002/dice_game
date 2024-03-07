from intelligence import Intelligence
import time


class Hard(Intelligence):
    def __init__(self, delay) -> None:
        """Init for Hard class"""
        self.delay = delay
        super().__init__()

    def playing_logic(self, total_score: int, current_score: int):
        """Playing logic for choice (Roll or Hold)"""
        round_score = self.calc_round_score(total_score, current_score)

        if round_score < 9 and current_score < 100:
            choice = "r"

        elif round_score >= 9 and current_score < 100:
            choice = "h"

        elif current_score >= 100:
            choice = "h"

        if choice == "r":
            time.sleep(1 * self.delay)
            print("Roll")
            time.sleep(1 * self.delay)
        else:
            time.sleep(1 * self.delay)
            print("Hold")
            time.sleep(1 * self.delay)
        return choice
