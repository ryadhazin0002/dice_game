from player import Player
from intelligence import Intelligence


class COPlayer(Player):
    # 🤖
    def __init__(self, level: Intelligence):
        """Constructor for CoPlayer class"""
        super().__init__("CO", 0)
        self.level = level

    level: Intelligence

    def take_action(self, current_score: int):
        """Take action for CoPlayer"""
        return self.level.playing_logic(self.total_score, current_score)
