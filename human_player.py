from player import Player


class HumanPlayer(Player):

    id: str
    high_scores: list[str]

    def __init__(self, id, name, high_scores):
        super().__init__(name, 0)
        self.id = id
        self.high_scores = high_scores

    def take_action(self):
        return input("Roll again or Hold? 'r' or 'h': ").rstrip()
