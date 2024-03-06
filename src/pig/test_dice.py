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


if __name__ == '__main__':
    unittest.main()
