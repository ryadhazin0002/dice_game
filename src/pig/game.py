import curses
import time
from co_player import COPlayer
from dice import Dice
from human_player import HumanPlayer
from in_venv import in_venv
from player import Player
from file_service import FileService
import random
from easy_level import Easy
from hard_level import Hard
from display import Display


class Game:

    def __init__(self, players, delay, filename: str) -> None:
        """Init for Game Class"""
        self.players = players
        self.fileService = FileService(filename)
        self.delay = delay
        self.display = Display(delay)
        pass

    players: list[HumanPlayer]

    def change_player_name(self, new_name: str, player: HumanPlayer):
        """Change player name"""
        player.name = new_name
        try:
            self.fileService.save_players(self.players)
        except FileNotFoundError:
            print("An error occurred while trying to change player's name in the file.")

    def get_player(self, name: str) -> HumanPlayer | None:
        """Get player name"""
        for player in self.players:
            if name == player.name:
                return player

    def add_player(self, name: str) -> HumanPlayer:
        """Add player to players list and players.txt if player is not already exsist"""
        player = self.get_player(name)
        if player is not None:
            return player
        player = HumanPlayer(random.randint(1000000, 5000000), name, [])
        try:
            self.fileService.add_player(player)
            self.players.append(player)
        except FileNotFoundError:
            print("An error occurred while trying to add new player to the file.")
        return player

    def init_players(self, playing_mode: str) -> tuple[Player, Player]:
        """Players initialization"""
        player1_name = input("Please enter your name: ")
        player1: Player = self.add_player(player1_name)
        player2: Player
        if playing_mode == "1":
            print("1. Easy")
            print("2. Hard")
            level = input("Your choice: ")
            if level == "1":
                intelligence: Easy = Easy(self.delay)
                player2 = COPlayer(intelligence)
            elif level == "2":
                intelligence: Hard = Hard(self.delay)
                player2 = COPlayer(intelligence)
        else:
            player2_name = input("Please enter the second player name: ")
            player2 = self.add_player(player2_name)
        return player1, player2

    def start(self):
        """The start menu"""
        while True:
            choice = self.display.display_main_menu()
            if choice == "1":
                playing_mode = self.display.display_new_game_menu()
                players: tuple[Player, Player] = self.init_players(playing_mode)
                self.play(players[0], players[1])
                try:
                    self.fileService.save_players(self.players)
                except FileNotFoundError:
                    print("An error occurred while trying to update the file.")
            elif choice == "2":
                self.display_players_highscore()
            elif choice == "3":
                self.display.display_game_rules()
            elif choice == "4":
                old_name = input("Enter your current name: ")
                new_name = input("Enter your new name: ")
                player = self.get_player(old_name)
                if player is not None:
                    self.change_player_name(new_name, player)
            elif choice == "5":
                break
            else:
                print("invalid value!!")
                print("Please enter 1, 2, 3 or 4")
                time.sleep(1 * self.delay)
                print()

    def play(self, first_player: Player, second_player: Player):
        """Play the game"""
        current_player: Player = first_player
        dice = Dice(self.delay)
        current_player_score = 0
        try:
            print(f"🔥🔥🔥 {current_player.name} turn 🔥🔥🔥")
        except:
            print(f" {current_player.name} turn ")
        while True:
            diceValue = 1
            if not in_venv():
                stdscr = curses.initscr()
                curses.noecho()
                curses.cbreak()
                diceValue = dice.roll_dice(stdscr)
            else:
                diceValue = random.randint(1, 6)
            dice.print_to_terminal(diceValue)
            if diceValue != 1:
                current_player_score += diceValue
                self.display.display_dice_value_and_round_score(
                    diceValue, current_player_score
                )
                roll_again = current_player.take_action(current_player_score)
                print(f"Roll again is {roll_again}")
                if roll_again == "r":
                    time.sleep(2 * self.delay)
                    continue
                elif roll_again == "h":
                    current_player.total_score = current_player_score
                    print(
                        f"{current_player.name}'s total"
                        f" score is {current_player.total_score}"
                    )
                    if max(first_player.total_score, second_player.total_score) >= 100:
                        winner: Player
                        if first_player.total_score > second_player.total_score:
                            winner = first_player
                        elif second_player.total_score > first_player.total_score:
                            winner = second_player
                        else:
                            self.display.display_draw()
                            break

                        self.display.display_congratulations(winner)
                        if isinstance(winner, HumanPlayer):
                            winner.high_scores.append(str(winner.total_score))
                        break
                    print("***************************************************")
                    time.sleep(2 * self.delay)
                    current_player = self.change_current_player(
                        current_player, first_player, second_player
                    )
                    current_player_score = current_player.total_score
                    try:
                        print(f"🔥🔥🔥 {current_player.name} turn 🔥🔥🔥")
                    except:
                        print(f" {current_player.name} turn ")
                    time.sleep(2 * self.delay)
                    continue
                elif roll_again == "CHEAT":
                    current_player.total_score += 90
                    current_player_score += 90
                    continue
                elif roll_again == "Q":
                    break
                elif roll_again == "R":
                    first_player.total_score = 0
                    second_player.total_score = 0
                    current_player_score = 0

            elif diceValue == 1:
                current_player = self.change_current_player(
                    current_player, first_player, second_player
                )
                current_player_score = current_player.total_score
                print("You have lost your round score!!!")
                print("******************************************************")
                time.sleep(2 * self.delay)
                try:
                    print(f"🔥🔥🔥 {current_player.name} turn 🔥🔥🔥")
                except:
                    print(f" {current_player.name} turn ")
                time.sleep(2 * self.delay)
                print(f"your score is {current_player_score}")
                time.sleep(1 * self.delay)

    def display_players_highscore(self):
        """Display player's highscore"""
        for player in self.players:
            high_scores = player.high_scores
            if len(high_scores) == 0:
                high_scores = None
            print(f"{player.name} : ", end="")
            if high_scores is None:
                print(None)
            else:
                high_scores.sort(reverse=True)
                print(str.join(" , ", high_scores))

    def change_current_player(
        self, current_player: Player, first_player: Player, second_player: Player
    ):
        """Change the current player"""
        if current_player.name == first_player.name:
            current_player = second_player
        else:
            current_player = first_player
        return current_player
