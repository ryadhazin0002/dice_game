from intelligence import Intelligence
import time

class Hard(Intelligence):
    def __init__(self) -> None:
        super().__init__()

    def playing_logic(self, total_score: int, current_score: int):
        round_score = self.calc_round_score(total_score, current_score)
        
        if round_score < 9 and current_score < 100:
            choice = "r"
            
        elif round_score >= 9:
            choice = "h"
            
        elif current_score >= 100:
            choice = "h"

        if choice == "r":
            time.sleep(1)
            print("Roll")
            time.sleep(1)
        else:
            time.sleep(1)
            print("Hold")
            time.sleep(1)
        return choice
