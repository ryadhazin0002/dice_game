from unittest.mock import patch
import unittest

from human_player import HumanPlayer


class TestHumanPlayerClass(unittest.TestCase):
    """Test the class."""

    def test_init_defult_human_player(self):
         """Instantiate an object and check its properties."""
         player = HumanPlayer("6546546", "player test", [])
         self.assertIsInstance(player, HumanPlayer)
         self.assertEqual(player.id, "6546546")
         self.assertEqual(player.name, "player test")
         self.assertListEqual(player.high_scores, [])

    @patch('builtins.input', side_effect=['r'])
    def test_take_action_roll(self, mock_input):
        player = HumanPlayer(id="1", name="John", high_scores=[100, 200])
        action = player.take_action(current_score=10)
        self.assertEqual(action, 'r')

    @patch('builtins.input', side_effect=['h'])
    def test_take_action_hold(self, mock_input):
        player = HumanPlayer(id="1", name="John", high_scores=[100, 200])
        action = player.take_action(current_score=10)
        self.assertEqual(action, 'h')

    @patch('builtins.input', side_effect=['invalid', 'wrong','123', 'p','r'])
    def test_take_action_invalid_then_roll(self, mock_input):
        player = HumanPlayer(id="1", name="John", high_scores=[100, 200])
        action = player.take_action(current_score=10)
        self.assertEqual(action, 'r')


if __name__ == "__main__":
    unittest.main()
    