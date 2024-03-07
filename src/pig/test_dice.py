import unittest
from unittest.mock import patch
import random
from io import StringIO
import time

from dice import Dice

class TestDice(unittest.TestCase):

    def test_print_to_terminal(self):
        dice = Dice(0)
        expected_output_3 = [
            "+-------+",
            "| o     |",
            "|   o   |",
            "|     o |",
            "+-------+",
        ]

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
 
            dice.print_to_terminal(3)

            actual_output = mock_stdout.getvalue().strip()

            for expected_line in expected_output_3:
                if expected_line.strip() == "|       |":
                    continue 
                self.assertIn(expected_line.strip(), actual_output)

    def test_roll_dice(self):
        dice = Dice(0)
        dice.roll_dice(None)  


if __name__ == '__main__':
    unittest.main()
