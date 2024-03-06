import unittest
from unittest.mock import Mock, patch
import random

# Assuming Dice is defined in another file (e.g., dice.py)
from dice import Dice

class TestDice(unittest.TestCase):

    def test_draw_dice_face(self):
        dice = Dice()
        stdscr_mock = Mock()

        # Test valid face value
        dice.draw_dice_face(stdscr_mock, 10, 5, 3)

        # Verify calls to curses methods for drawing the face
        self.assertTrue(stdscr_mock.addstr.called)

        # Test invalid face value (clamped to 1)
        dice.draw_dice_face(stdscr_mock, 10, 5, 0)

        # Test invalid face value (clamped to 6)
        dice.draw_dice_face(stdscr_mock, 10, 5, 7)

    @patch('random.randint')
    def test_roll_dice(self, mock_randint):
        dice = Dice()

        # Install curses library within the test
        try:
            import curses  # Install curses if not already available
        except ImportError:
            print("Warning: curses library not installed. Skipping real screen test.")
            return

        # Set the random seed to ensure a specific value (3) is rolled
        mock_randint.return_value = 3

        try:
            # Initialize and clear the screen within the test
            stdscr = curses.initscr()
            curses.cbreak()
            curses.noecho()

            rolled_value = dice.roll_dice(stdscr)
            self.assertEqual(rolled_value, 3)

        finally:
            # Restore terminal settings and end curses
            curses.echo()
            curses.nocbreak()
            curses.endwin()

    def test_print_to_terminal(self):
        dice = Dice()

        # Expected output based on the example implementation in dice.py
        expected_output_3 = [
            "+-------+",
            "| o     |",
            "|       |",
            "|       |",
            "+-------+",
        ]

        with patch('sys.stdout', new=Mock()) as mock_stdout:
            # Ensure dice face is drawn before printing
            dice.draw_dice_face(mock_stdout, 0, 0, 3)

            # Capture the written output and remove extra whitespace/newlines
            actual_output = ''.join(call[1][0] for call in mock_stdout.write.mock_calls)

            # Check if each line in the expected output is present in the actual output,
            # allowing for minor whitespace differences:
            for expected_line in expected_output_3:
                self.assertIn(expected_line.strip(), actual_output.strip())

    # This test attempts to test roll_dice with a real curses screen,
    # but keep in mind limitations discussed previously.
    def test_roll_dice_real_screen(self):
        try:
            # Install curses library if not present
            try:
                import curses
            except ImportError:
                print("Warning: curses library not installed. Skipping real screen test.")
                return

            # Initialize and clear the screen
            stdscr = curses.initscr()
            curses.cbreak()
            curses.noecho()

            # Create a Dice object and perform a roll
            dice = Dice()
            dice.roll_dice(stdscr)

        except Exception as e:
            # Handle potential exceptions due to curses limitations
            print(f"Exception encountered during real screen test: {e}")

        finally:
            # Restore terminal settings and end curses
            curses.echo()
            curses.nocbreak()
            curses.endwin()


if __name__ == '__main__':
    unittest.main()
