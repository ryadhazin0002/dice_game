import curses
import random
import time

def draw_dice_face(stdscr, x, y, face_value):
    """Draws a dice face with the given value at the specified location."""
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

    # Ensure face value is between 1 and 6
    face_value = max(1, min(6, face_value))

    for row in range(len(dice_faces[face_value])):
        stdscr.addstr(y + row, x, dice_faces[face_value][row])

def roll_dice(stdscr):
    """Rolls a dice, draws it on the screen, and waits before repeating."""
    while True:
        # Clear the screen
        stdscr.clear()

        # Roll the dice
        roll = random.randint(1, 6)

        # Draw the dice face
        draw_dice_face(stdscr, 20, 10, roll)
        stdscr.refresh()

        # Wait 2 seconds
        time.sleep(0.1)

        # Clear the dice drawing for next roll
        for row in range(5):
            stdscr.addstr(10 + row, 20, " " * 9)

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
try:
    roll_dice(stdscr)
except KeyboardInterrupt:
    pass
finally:
    curses.echo()
    curses.nocbreak()
    curses.endwin()