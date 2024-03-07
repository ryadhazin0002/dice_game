# 🎲Pig Dice Game🎲
## 📜Description📜:
This Python program implements a text-based version of the Pig Dice Game, where players take turns rolling a dice and accumulating points to reach a target score.
## ✨Features✨:
* Single-player mode against a computer opponent (COPlayer) with different levels of intelligence.
* Multiplayer mode where two human players can compete against each other.
* Simple and intuitive user interface through the terminal.
* Option to change player names and view high scores.

## ⚙️Installation⚙️:

* Clone the repository to your local machine:

 ```bash
git clone <https://github.com/ryadhazin0002/dice_game.git>
```
* Ensure you have Python 3 installed.
* Navigate to the project directory:
``` bash
cd dice_game
```
* Run the makefile to install dependencies and setup the invironment:
```bash
make install
````
* Navigate to the game directory:
```bash
cd src/pig
```

## 🎮Usage🎮:
* Run the game:
``` bash
python main.py
```
* Follow the on-screen instructions to start a new game, view high scores, read game rules, or exit.



## 🎲Game Rules🎲

- Objective: Be the first player to reach a total score of 100 points.
- Players take turns rolling a dice during their turn.
- Rolling a 1 forfeits all points gained in that turn.
- The first player to reach or exceed 100 points wins the game.

## 💾File Structure💾

- `main.py`: Entry point of the program.
- `player.py`: Abstract base class for game players.
- `human_player.py`: Implementation of the human player class.
- `co_player.py`: Implementation of the computer opponent (COPlayer) class.
- `intelligence.py`: Abstract base class for player intelligence.
- `easy_level.py`: Implementation of easy intelligence level for COPlayer.
- `hard_level.py`: Implementation of hard intelligence level for COPlayer.
- `dice.py`: Class for simulating dice rolls.
- `display.py`: Class for displaying game-related messages.
- `file_service.py`: Class for handling file operations (e.g., loading/saving players' data).

## 📚Credits📚

- This project uses Python's `curses` library for terminal-based UI.

## 🔑License🔑

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧Contact Information📧

For inquiries or support, please contact.

[ryad.hazin0002@stud.hkr.se](mailto:ryad.hazin0002@stud.hkr.se)

[mustafa.al-bayati0036@stud.hkr.se](mailto:mustafa.al-bayati0036@stud.hkr.se)

[zakaria.majkouma0013@stud.hkr.se](mailto:zakaria.majkouma0013@stud.hkr.se)