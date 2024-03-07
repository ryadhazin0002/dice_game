import io
import sys
import unittest
from unittest.mock import patch

from display import Display
from human_player import HumanPlayer


class TestDisplay(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        self.display = Display(0)
        super().__init__(methodName)

    def test_draw(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        self.display.display_draw()

        sys.stdout = sys.__stdout__

        output = capturedOutput.getvalue()
        self.assertEqual("DRAW" in output, True)
        self.assertEqual(output.count("\n"), 3)

    def test_congratulations(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        self.display.display_congratulations(HumanPlayer("0", "Winner", []))

        sys.stdout = sys.__stdout__

        output = capturedOutput.getvalue()
        self.assertEqual("congratulations" in output, True)
        self.assertEqual(output.count("\n"), 3)

    @patch("builtins.input", side_effect=["1"])
    def test_co_player_level(self, mock_input):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        self.display.display_co_player_level()

        sys.stdout = sys.__stdout__

        output = capturedOutput.getvalue()
        self.assertEqual("1. Easy" in output, True)
        self.assertEqual("2. Hard" in output, True)
        self.assertEqual(output.count("\n"), 2)

    def test_rules(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        self.display.display_game_rules()

        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        self.assertEqual("Pig Dice Game Rules" in output, True)
        self.assertEqual("Gameplay" in output, True)
        self.assertEqual("Winning" in output, True)
        self.assertEqual("Strategy" in output, True)
        self.assertEqual(output.count("\n"), 20)
