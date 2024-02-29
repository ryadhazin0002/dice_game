from player import Player
from intelligence import Intelligence
from easy_level import Easy


class COPlayer(Player):

    def __init__(self, level: Intelligence):
        super().__init__("🤖", 0)
        self.level = level

    level: Intelligence

    def take_action(self, current_score: int):
        """Take action for CoPlayer"""
        return self.level.playing_logic(self.total_score, current_score)
