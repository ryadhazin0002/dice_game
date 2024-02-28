import curses
import random
import time


class Dice:

    def __init__(self) -> None:
        pass

    dice_faces = {
            1: [
                "+-------+",
                "|       |",
                "|   o   |",
                "|       |",
                "+-------+",
            ],
            2: [
                "+-------+",
                "| o     |",
                "|       |",
                "|     o |",
                "+-------+",
            ],
            3: [
                "+-------+",
                "| o     |",
                "|   o   |",
                "|     o |",
                "+-------+",
            ],
            4: [
                "+-------+",
                "| o   o |",
                "|       |",
                "| o   o |",
                "+-------+",
            ],
            5: [
                "+-------+",
                "| o   o |",
                "|   o   |",
                "| o   o |",
                "+-------+",
            ],
            6: [
                "+-------+",
                "| o   o |",
                "| o   o |",
                "| o   o |",
                "+-------+",
            ],
        }

    def draw_dice_face(self, stdscr, x, y, face_value):
        """Draws a dice face with the given value at the specified location."""

        # Ensure face value is between 1 and 6
        face_value = max(1, min(6, face_value))

        try:
            for row in range(len(self.dice_faces[face_value])):
                stdscr.addstr(y + row, x, self.dice_faces[face_value][row])
        except:
            pass

    def roll_dice(self, stdscr) -> int:
        """Rolls a dice, draws it on the screen, and waits before repeating."""
        current_roll = 0
        current_dice_value = 1
        try:
            while current_roll < 10:
                current_roll += 1
                # Clear the screen
                stdscr.clear()

                # Roll the dice
                current_dice_value = random.randint(1, 6)

                # Draw the dice face
                self.draw_dice_face(stdscr, 20, 10, current_dice_value)
                stdscr.refresh()

                # Wait 2 seconds
                time.sleep(0.25)

                # Clear the dice drawing for next roll
                try:
                    for row in range(5):
                        stdscr.addstr(10 + row, 20, " " * 9)
                except:
                    pass
        except KeyboardInterrupt:
            pass
        finally:
            curses.echo()
            curses.nocbreak()
            curses.endwin()

        return current_dice_value

    def print_to_terminal(self, desiredValue: int):
        desiredFace = self.dice_faces[desiredValue]
        for row in range(len(desiredFace)):
            print(desiredFace[row])
