import unittest
from unittest.mock import Mock, patch
import random
from io import StringIO
import time

from dice import Dice

class TestDice(unittest.TestCase):
    def test_draw_dice_faces(self):
        dice = Dice()
        try:
            import curses  
        except:
            pass

        try:
            stdscr = curses.initscr()
            curses.cbreak()
            curses.noecho()


            for face_value in dice.dice_faces:
                stdscr.clear() 
                dice.draw_dice_face(stdscr, 10, 5, face_value)
                stdscr.refresh()
                time.sleep(1)
                expected_output = dice.dice_faces[face_value]
                for row, expected_row in enumerate(expected_output):
                    self.assertIn(expected_row.strip(), stdscr.instr(5 + row, 10, len(expected_row)).decode().strip())

        finally:
            curses.echo()
            curses.nocbreak()
            curses.endwin()
    @patch('random.randint')
    def test_roll_dice(self, mock_randint):
        dice = Dice()
        try:
            import curses  
        except ImportError:
            print("Warning: curses library not installed. Skipping real screen test.")
            return

        mock_randint.return_value = 3

        try:
            stdscr = curses.initscr()
            curses.cbreak()
            curses.noecho()

            rolled_value = dice.roll_dice(stdscr)
            self.assertEqual(rolled_value, 3)

        finally:
            curses.echo()
            curses.nocbreak()
            curses.endwin()

    def test_print_to_terminal(self):
        dice = Dice()
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
            


if __name__ == '__main__':
    unittest.main()
