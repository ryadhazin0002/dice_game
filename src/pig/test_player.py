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
        
        
    def test_concrete_player_fail(self):
        player = ConcretePlayer("Micke", 100)
        result = player.take_action(60)
        self.assertEqual(result, "h", "Expected 'h' but got {}".format(result))
        self.assertNotEqual(result, "r", "Expected 'h' but got 'r'")
    
    def test_concrete_player_edge_case(self):
        player = ConcretePlayer("Anderas", 100)
        result = player.take_action(50)
        self.assertEqual(result, "h", "Expected 'h' but got {}".format(result))
        self.assertNotEqual(result, "r", "Expected 'h' but got 'r'")
    
    def test_player_attributes(self):
        player = ConcretePlayer("Braco", 100)
        self.assertTrue(player, 'name')
        self.assertTrue(player, 'total_score')
        self.assertEqual(player.name, "Braco")
        self.assertEqual(player.total_score, 100)
        
        







if __name__ == '__main__':
    unittest.main()
