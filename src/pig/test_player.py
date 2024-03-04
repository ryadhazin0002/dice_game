import unittest
from player import Player
from abc import ABC

class Player(ABC):
    class TestPlayer(unittest.TestCase):
        def setUp(self):
            self.player = Player("TestPlayer", 0)
        
    def test_player_creation(self):
        self.assertEqual(self.player.name, "TestPlayer")
        self.assertEqual(self.player.total_score, 0)
        
    def test_take_action_abstract(self):
        with self.assertRaises(TypeError):
            self.player.take_action(10)
        


if __name__ == '__main__':
    unittest.main()
    