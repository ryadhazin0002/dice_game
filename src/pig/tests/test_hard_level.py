import unittest
from unittest.mock import patch
from hard_level import Hard
import time


class TestHardLevel(unittest.TestCase):
    @patch("builtins.print")
    def test_playing_logic_roll(self, mocked_print):
        hard_instance = Hard(0)
        choice = hard_instance.playing_logic(35, 40)
        self.assertEqual(choice, "r")
        self.assertIsNot(choice, "h")
        mocked_print.assert_called_with("Roll")

    @patch("builtins.print")
    def test_playing_logic_hold(self, mocked_print):
        hard_instance = Hard(0)
        choice = hard_instance.playing_logic(40, 50)
        self.assertEqual(choice, "h")
        self.assertIsNot(choice, "r")
        mocked_print.assert_called_with("Hold")

    @patch("builtins.print")
    def test_playing_logic_hold_100(self, mocked_print):
        hard_instance = Hard(0)
        choice = hard_instance.playing_logic(99, 115)
        self.assertEqual(choice, "h")
        self.assertIsNot(choice, "r")
        mocked_print.assert_called_with("Hold")

    @patch("builtins.print")
    def test_playing_logic_minimum_scores(self, mocked_print):
        hard_instance = Hard(0)
        choice = hard_instance.playing_logic(0, 0)
        self.assertEqual(choice, "r")
        self.assertIsNot(choice, "h")
        mocked_print.assert_called_with("Roll")

    @patch("builtins.print")
    def test_playing_logic_max_score(self, mocked_print):
        hard_instance = Hard(0)
        choice = hard_instance.playing_logic(100, 100)
        self.assertEqual(choice, "h")
        self.assertIsNot(choice, "r")
        mocked_print.assert_called_with("Hold")

    def test_error_handling_incorrect_data_types(self):
        hard_instance = Hard(0)
        with self.assertRaises(TypeError):
            hard_instance.playing_logic("total_score", "current_score")
        with self.assertRaises(TypeError):
            hard_instance.playing_logic(35, "current_score")
        with self.assertRaises(TypeError):
            hard_instance.playing_logic("total_score", 40)

    def test_playing_logic_not_none(self):
        hard_instance = Hard(0)
        choice = hard_instance.playing_logic(30, 40)
        self.assertIsNotNone(choice)


if __name__ == "__main__":
    unittest.main()
