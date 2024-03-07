import unittest
from intelligence import Intelligence
from hard_level import Hard
from easy_level import Easy
from co_player import COPlayer
import random


class TestCOPlayer(unittest.TestCase):

    def test_co_player_init(self):
        level = random.choice([Easy(0), Hard(0)])
        co_player = COPlayer(level)

        self.assertEqual(co_player.name, "CO")
        self.assertEqual(co_player.total_score, 0)
        self.assertEqual(co_player.level, level)
        self.assertIsInstance(co_player, COPlayer)

    def test_take_action(self):
        level = random.choice([Easy(0), Hard(0)])
        co_player = COPlayer(level)
        current_score = 10
        choice = ["r", "h"]
        result = co_player.take_action(current_score)
        self.assertIn(result, choice)
        self.assertIsInstance(result, str)
        self.assertIsNotNone(result, None)


if __name__ == "__main__":
    unittest.main()
