from intelligence import Intelligence


class Hard(Intelligence):
    def __init__(self) -> None:
        super().__init__()

    def playing_logic(self, total_score: int, current_score: int):
        round_score = self.calc_round_score(total_score, current_score)
        return "hard"
