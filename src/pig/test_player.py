import unittest
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name, total_score):
        self.name = name
        self.total_score = total_score

    @abstractmethod
    def take_action(self, current_score: int):
        """Abstract take action method"""
        pass


class ConcretePlayer(Player):
    def take_action(self, current_score: int):
        if current_score < 50:
            return "r"
        else:
            return "h"
class TestPlayer(unittest.TestCase):
    def test_concrete_player_pass(self):
        player = ConcretePlayer("Pelle", 100)
        result = player.take_action(40)
        self.assertEqual(result, "r", "Expected 'r' but got {}".format(result))
        self.assertNotEqual(result, "h", "Expected 'r' but got 'h'")






if __name__ == '__main__':
    unittest.main()
