from player import Player


class HumanPlayer(Player):

    id: str
    high_scores: list[str]

    def __init__(self, id, name, high_scores):
        """Init for HumanPlayer class"""
        super().__init__(name, 0)
        self.id = id
        self.high_scores = high_scores

    def take_action(self, current_score: int):
        """Take action for HumanPlayer"""
        choice = ""
        while choice not in ["r", "h", "Q", "R", "CHEAT"]:
            choice = input("Roll again or Hold? 'r' or 'h': ").rstrip()
            if choice not in ["r", "h", "Q", "R", "CHEAT"]:
                print("Invalid choice ")
        return choice
