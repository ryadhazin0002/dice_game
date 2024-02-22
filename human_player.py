from player import Player

class HumanPlayer(Player):

    id: str

    def __init__(self, id,name, total_score):
        super().__init__(name, total_score)
        self.id = id

    def take_action(self):
        return input("Roll again or Hold? 'r' or 'h': ").rstrip()